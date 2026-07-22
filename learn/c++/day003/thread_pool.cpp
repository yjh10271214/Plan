#include <iostream>
#include <mutex>
#include <condition_variable>
#include <thread>
#include <queue>
#include <functional>
#include <atomic>
#include <vector>
#include <cstdio>
#include <chrono>

class ThreadPool {
private:
    std::vector<std::thread> mWorkers;   //工作线程集合
    std::queue<std::function<void()>> mTasks;    //任务队列
    
    std::mutex mQueueMtx;   //任务队列锁
    std::condition_variable mCv; //通知工作线程
    std::atomic<bool> mStopFlag{false}; //原子标志位通知所有线程退出

public:
    ThreadPool(int thread_count = 4) {
        for (int i = 0; i < thread_count; ++i) {
            mWorkers.emplace_back([this](){
                while (true) {
                    std::function<void()> task;
                    {
                        std::unique_lock<std::mutex> lock(mQueueMtx);
                        mCv.wait(lock, [this](){
                            return mStopFlag.load() || !mTasks.empty();
                        });

                        if (mStopFlag.load() && mTasks.empty())
                            return;

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
        mCv.notify_all(); //唤醒所有等待工作的线程
        
        for (std::thread& worker : mWorkers) {
            if (worker.joinable())
                worker.join();
        }
    }

    template <typename Func>
    void add(Func&& f) {
        {
            std::lock_guard<std::mutex> lock(mQueueMtx);
            mTasks.emplace(std::forward<Func>(f));
        }
        mCv.notify_one();
    }
    int size() const { return mWorkers.size(); }
};

int main() {
    using namespace std::chrono_literals;
    ThreadPool pool(4);
    std::cout << "ThreadPool created, worker threads: " << pool.size() << std::endl;

    for (int i = 0; i < 10; ++i) {
        pool.add([i](){
            std::cout << "Task " << i << " running on thread " << std::this_thread::get_id() << std::endl;
            std::this_thread::sleep_for(100ms); // 模拟任务耗时
        });
    }
    return 0;
}