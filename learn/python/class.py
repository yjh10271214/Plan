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
