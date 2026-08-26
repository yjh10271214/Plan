class Student:
    """学生"""
    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def study(self, course_name):
        """学习"""
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        """玩耍"""
        print(f'{self.name}正在玩游戏.')

class Student:
    __slots__ = ('name', 'age') #希望在使用对象时动态的为对象添加属性

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student:

    def __init__(self, name, age):
        self.__name = name #__私有属性, _受保护属性
        self.__age = age

    def study(self, course_name):
        print(f'{self.__name}正在学习{course_name}.')

stu = Student('王大锤', 20)
stu.study('Python程序设计')
#print(stu.__name)  AttributeError（属性错误）异常， stu._Student__name的方式仍然可以访问到私有属性


"""
可以直接使用类名.方法名的方式来调用静态方法和类方
二者的区别在于，类方法的第一个参数是类对象本身，而静态方法则没有这个参数。
简单的总结一下，对象方法、类方法、静态方法都可以通过“类名.方法名”的方式来调用，
区别在于方法的第一个参数到底是普通对象还是类对象，还是没有接受消息的对象
"""
class Triangle(object):
    """三角形"""

    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and a + c > b

    # @classmethod
    # def is_valid(cls, a, b, c):
    #     """判断三条边长能否构成三角形(类方法)"""
    #     return a + b > c and b + c > a and a + c > b

    @property #property wrapper 对象不再通过调用方法而是访问属性的方式 t.perimeter() -> t.perimeter
    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c
    @property
    def area(self):
        """计算面积"""
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
      

if Triangle.is_valid(3, 4, 5):
    t = Triangle(3, 4, 5)
    print(f'周长: {t.perimeter}')
    print(f'面积: {t.area}')
else:
    print('无效的边长!!!')


class Person:
    """人"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f'{self.name}正在吃饭.')
    
    def sleep(self):
        print(f'{self.name}正在睡觉.')


class Student(Person):
    """学生"""
    
    def __init__(self, name, age):
        super().__init__(name, age) #重写了__init__不执行就没有父类的属性
    
    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title
    
    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}.')



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(3, 5)
print(str(p))   # Point(3, 5)
print(repr(p))  # Point(3, 5)
print(p)        # Point(3, 5)，print 会自动调用 __str__
#__str__ 面向用户，可读性好。
#__repr__ 面向开发者，通常能唯一标识对象。
#如果只定义 __repr__，__str__ 会默认使用 __repr__。


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property #限制私有变量的权限
    def radius(self):
        """获取半径"""
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("半径不能为负")
        self._radius = value

c = Circle(5)
print(c.radius)   # 5，直接访问，无需括号
c.radius = 10     # 调用 setter
print(c.radius)   # 10
# c.radius = -1   # 抛出 ValueError


class Person:
    def __init__(self, name):
        self._name = name      # 约定私有
        self.__age = 0          # 名称改写

p = Person("Tom")
print(p._name)      # Tom，虽然约定私有但能访问
# print(p.__age)    # 报错，因为改名为 _Person__age
print(p._Person__age)  # 0，可以绕过


