#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <queue>
#include <chrono>
#include <atomic>
#include <vector>
#include <functional>
#include <future>

struct SensorData {
    int sensor_id;
    double temperature;
    std::string timestamp;

    SensorData(int id, double temp, std::string ts)
        : sensor_id(id), temperature(temp), timestamp(ts){}
    
    virtual ~SensorData() = default;
};

class ThreadPool {
private:
    std::vector<std::thread> mWorkers;
    std::queue<std::function<void()>> mTasks;

    std::mutex mQueueMtx;
    std::condition_variable mCv;
    std::atomic<bool> mStopFlag{false};

public:
    explicit ThreadPool(std::size_t threads_count = 4) {
        for (std::size_t i = 0; i < threads_count; ++i) {
            mWorkers.emplace_back([this](){
                while (true) {
                    std::function<void()> task;
                    {
                        std::unique_lock<std::mutex> lock(mQueueMtx);
                        mCv.wait(lock, [this](){
                            return mStopFlag.load() || !mTasks.empty();
                        });

                        if (mStopFlag.load() && mTasks.empty()) {
                            return;
                        }

                        task = std::move(mTasks.front());
                        mTasks.pop();
                    }

                    task();
                }
            });
        }
    }

    ~ThreadPool() {
        mStopFlag.store(true);
        mCv.notify_all();
        for (std::thread& worker : mWorkers) {
            if (worker.joinable()) {
                worker.join();
            }
        }
    }

    template <typename Func, typename... Args>
    auto submit(Func&& f, Args&&... args)
        -> std::future<typename std::result_of<Func(Args...)>::type>
    {
        using ReturnType = typename std::result_of<Func(Args...)>::type;
         // 1. 创建一个 packaged_task，包装用户传入的函数和参数
        //    使用 shared_ptr 是因为 packaged_task 不可拷贝，需要分配到堆上
        auto taskPtr = std::make_shared<std::packaged_task<ReturnType()>>(
            std::bind(std::forward<Func>(f), std::forward<Args>(args)...)
        );
         // 2. 拿到与 packaged_task 关联的 future，返回给调用者
        std::future<ReturnType> result = taskPtr->get_future();

         // 3. 将 packaged_task 包装成 void() 任务，入队
        {
            std::lock_guard<std::mutex> lock(mQueueMtx);
            mTasks.emplace([taskPtr]() {
                (*taskPtr)(); // 执行 packaged_task，结果自动写入 future
            });
        }
        mCv.notify_one();
        return result;
    }

    size_t size() const { return mWorkers.size(); }
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

int add(int a, int b) {
    std::this_thread::sleep_for(std::chrono::seconds(1));
    return a + b;
}

int main() {
    // SensorGateway gateway;
    // gateway.start();

    ThreadPool pool(4);

    // 提交任务，拿到 future
    auto f1 = pool.submit(add, 3, 4);
    auto f2 = pool.submit([](int x, int y) { return x * y; }, 5, 6);
    auto f3 = pool.submit([]() { 
        std::this_thread::sleep_for(std::chrono::milliseconds(500)); 
        return std::string("hello"); 
    });

    std::cout << "add(3,4) = " << f1.get() << std::endl;   // 输出 7，会阻塞等待任务完成
    std::cout << "5*6 = " << f2.get() << std::endl;         // 输出 30
    std::cout << "string: " << f3.get() << std::endl;       // 输出 hello
    return 0;
}