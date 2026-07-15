#include <iostream> 

template <typename T>
class SharedPointer {
public:
    explicit SharedPointer(T* ptr) 
            : mPtr(ptr ? ptr : nullptr), mRef(nullptr) {
                if (mPtr) {
                    mRef = new int(1);
                }
            }
    //移动构造
    SharedPointer(SharedPointer&& other)  noexcept 
            : mPtr(other.mPtr), mRef(other.mRef) {
                    other.mPtr = nullptr;
                    other.mRef = nullptr;
                }
    //拷贝构造
    SharedPointer(const SharedPointer& other) 
            : mPtr(other.mPtr), mRef(other.mRef) {
                    if (mRef) {
                        (*mRef)++;
                    }
                }

    ~SharedPointer() {
        release();
    }

    //移动赋值
    SharedPointer& operator=(SharedPointer&& other) {
        if (this != other) {
            release(); //释放自己拥有的资源
            mPtr = other.mPtr;
            mRef = other.mRef;
            other.mPtr = nullptr;
            other.mRef = nullptr;
        }
        return *this;
    }
    //拷贝赋值
    SharedPointer& operator=(const SharedPointer& other) {
        if (this != other) {
            release();
            mPtr = other.mPtr;
            mRef = other.mRef;
            if (mRef) {
                (*mRef)++;
            }
        }
        return *this;
    }

    T& operator*() const { return *mPtr; };
    T* operator->() const { return mPtr; };
    explicit operator bool () const { return mPtr ? true : false; };

    int use_count() const { return mRef ? *mRef : 0; }

    void release() {
        if (mRef) {
            (*mRef)--;
            if (*mRef == 0) {
                delete mRef;
                delete mPtr;
            }
            mRef= nullptr;
            mPtr = nullptr;
        }
    }
    
private:
    
private: 
    T* mPtr;
    int* mRef;
};

int main () {

    return 0;
}