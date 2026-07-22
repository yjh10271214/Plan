#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <queue>
#include <chrono>
#include <atomic>
#include <vector>
#include <functional>

struct SensorData {
    int sensor_id;
    double temperature;
    std::string timestamp;

    SensorData(int id, double temp, std::string ts)
        : sensor_id(id), temperature(temp), timestamp(ts){}
    
    virtual ~SensorData() = default;
};

template <typename T>
class SafeQueue {
    std::queue<T> mQue;
    std::mutex mMtx;
    std::condition_variable mCv;
    int mMaxSize;

public:
    explicit SafeQueue(int max_size = 100) : mMaxSize(max_size) {}

    //入队独队列满了就阻塞
    void push(T&& item) {
        std::unique_lock<std::mutex> lock(mMtx);
        mCv.wait(lock, [this](){ return mQue.size() < mMaxSize; });
        mQue.push(std::move(item));
        mCv.notify_one();
    }

    //出队
    T pop() {
        std::unique_lock<std::mutex> lock(mMtx);
        mCv.wait(lock, [this](){ return !mQue.empty(); });
        T item = std::move(mQue.front());
        mQue.pop();
        mCv.notify_one();
        return item;
    }

    bool tryPop(T& item) {
        std::lock_guard<std::mutex> lock(mMtx);
        if (mQue.empty()) return false;
        item = std::move(mQue.front());
        mQue.pop();
        return true;
    }

    T pop(std::atomic<bool>& running) {
        std::unique_lock<std::mutex> lock(mMtx);
        mCv.wait(lock, [this, &running]() { 
            return !mQue.empty() || !running.load(); 
        });
        // 如果是因停止被唤醒且队列为空，抛出异常或返回默认值
        if (mQue.empty()) {
            throw std::runtime_error("Queue stopped");
        }
        T item = std::move(mQue.front());
        mQue.pop();
        mCv.notify_one();
        return item;
    }

    bool empty() {
        std::lock_guard<std::mutex> lock(mMtx);
        return mQue.empty();
    }
};

//网关系统
class SensorGateway {
    SafeQueue<SensorData> mRawQueue;    //原始数据队列
    SafeQueue<SensorData> mResultQueue; //处理结果队列
    std::vector<std::thread> mWorkers;  //处理线程集合
    std::atomic<bool> mRunning{true};   //系统运行标志

    //采集线程函数
    void collectorMain() {
        int seq{0};
        while (mRunning.load()) {
            //模拟传感数据温度在20.0-30.0之间波动
            double temp = 20.0 + (rand() % 100) / 10.0;
            auto now = std::chrono::system_clock::now();
            time_t t = std::chrono::system_clock::to_time_t(now);
            std::string ts = std::ctime(&t);
            ts.pop_back(); //去掉换行符号

            mRawQueue.push(SensorData(1, temp, ts));
            std::cout << "[采集] 温度=" << temp << "°C, 时间=" << ts << std::endl;

            std::this_thread::sleep_for(std::chrono::milliseconds(500));
            seq++;
            if (seq >= 20) break;
        }
        std::cout << "[采集] 采集线程退出" << std::endl;
    }

    void processorMain(int worker_id) { //处理函数主线程
        while (mRunning.load()) {
            SensorData raw = mRawQueue.pop();
            if (!mRunning.load()) break; //停止后不在处理

             // 模拟数据处理：异常值滤波（超过 28 度的强制设为 28）
            double original = raw.temperature;
            if (raw.temperature > 28.0) {
                raw.temperature = 28.0;
            }

            std::cout << "[处理-" << worker_id << "] 原始=" << original 
                 << "°C, 滤波后=" << raw.temperature << "°C" << std::endl;
            
            mResultQueue.push(std::move(raw));
            std::this_thread::sleep_for(std::chrono::milliseconds(100));
        }
        std::cout << "[处理-" << worker_id << "] 处理线程退出" << std::endl;
    }

    void reporterMain() { //上报函数
        while (mRunning.load()) {
            SensorData result = mResultQueue.pop();
            if (!mRunning.load()) break;

            std::cout << "[上报] → 云端: 传感器" << result.sensor_id 
                 << ", 温度=" << result.temperature 
                 << "°C, 时间=" << result.timestamp << std::endl;
        }
        std::cout << "[上报] 上报线程退出" << std::endl;  // 补上这一行
    }

public:
    void start() { //启动系统
        std::cout << "===== 智能数据网关 v0.1 启动 =====" << std::endl;

        std::thread collector(&SensorGateway::collectorMain, this);
        std::thread reporter(&SensorGateway::reporterMain, this);

        for (int i = 0; i < 2; ++i) { // 启动 2 个处理线程
            mWorkers.emplace_back(&SensorGateway::processorMain, this, i+1);
        }

        collector.join();

        mRunning.store(false); // 采集线程结束后，设置停止标志，并唤醒所有阻塞的线程
        mRawQueue.push(SensorData(-1, -1, ""));      // 哨兵数据
        mRawQueue.push(SensorData(-1, -1, ""));      // 哨兵数据
        mResultQueue.push(SensorData(-1, -1, ""));   // 哨兵数据

        reporter.join();
        for (auto& w : mWorkers) {
            w.join();
        }

        std::cout << "===== 网关系统已安全关闭 =====" << std::endl;
    }
};

int main() {
    SensorGateway gateway;
    gateway.start();
    return 0;
}