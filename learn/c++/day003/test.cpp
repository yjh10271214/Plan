#include <iostream>
#include <vector>
#include <algorithm>
#include <thread>
#include <mutex>
#include <string>

class TicketSeller {
    int remaining{100};
    std::mutex mtx;
public:
    void sell(const std::string& name) {
        while (true) {
            {
                std::lock_guard<std::mutex> lock(mtx);
                if (remaining <= 0) break;
                std::cout << name << " 卖出第 " << remaining << " 张票\n";
                remaining--;
            }
            std::this_thread::sleep_for(std::chrono::seconds(1));
        }
    }
};

int main () {
    // std::vector<int> v{1, 2, 3, 4, 5, 6};
    // for_each(v.begin(), v.end(), [](int x){
    //     if (x % 2 == 0)
    //         std::cout << x << " ";
    // });
    // std::cout << std::endl;

    // sort(v.begin(), v.end(), [](int a, int b) { return a > b; });
    // for (int x : v) 
    //     std:: cout << x << " ";
    // std::cout << std::endl;
    TicketSeller ts;
    std::thread t1(&TicketSeller::sell, &ts, "窗口A");
    std::thread t2(&TicketSeller::sell, &ts, "窗口B");
    std::thread t3(&TicketSeller::sell, &ts, "窗口C");

    t1.join();
    t2.join();
    t3.join();
    std::cout << "所有票已售罄" << std::endl;
    return 0;
}