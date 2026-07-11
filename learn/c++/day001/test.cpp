#include <iostream>

class EmptyClass {

};

class Base {
public:
    Base() {
        func1();
    }
    virtual void func1() {
        std::cout << "Base func1" << std::endl;
    }
    virtual void func2() {
        std::cout << "Base func2" << std::endl;
    }
};

class Derived : public Base { //derived 衍生的 polymorphism 多态
public:
    Derived() {
        func1();
    }
    void func1() override {
        std::cout << "Derived func1" << std::endl;
    }

};

int main() {
    std::cout << "Size of empty class: " << sizeof(EmptyClass) << std::endl;
    std::cout << "Size of Base: " << sizeof(Base) << std::endl;
    std::cout << "Size of Derived: " << sizeof(Derived) << std::endl;

    Base b;
    Derived d;

    return 0;
}