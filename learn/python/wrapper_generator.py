import time

def timer(func):
    """装饰器：计算函数运行时间"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 耗时: {end - start:.4f} 秒")
        return result
    return wrapper

@timer
def my_function():
    time.sleep(0.5)
    print("函数执行")

my_function()



def repeat(n):
    """装饰器工厂：重复执行函数 n 次"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("hello")

say_hello()
# hello
# hello


from functools import wraps

def timer(func):
    @wraps(func)   # 保留原函数的元信息
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 耗时: {end - start:.4f} 秒")
        return result
    return wrapper

@timer
def my_function():
    """这是文档字符串"""
    time.sleep(0.1)

print(my_function.__name__)   # my_function，而不是 wrapper
print(my_function.__doc__)    # 这是文档字符串
# hello

# 常用装饰器
# @property         # 属性装饰器
# @staticmethod      # 静态方法
# @classmethod       # 类方法


def count_up(n):
    i = 0
    while i < n:
        yield i   # 产生一个值，暂停，下次从这里继续
        i += 1

# 调用生成器函数，返回生成器对象
gen = count_up(5)

print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2

# 可以用 for 循环遍历
for x in count_up(3):
    print(x)
# 0 1 2


# 列表推导式：立即生成完整列表
lst = [x*x for x in range(10)]

# 生成器表达式：惰性生成
gen = (x*x for x in range(10))

print(next(gen))   # 0
print(next(gen))   # 1


"""
可迭代对象：实现了 __iter__ 方法，返回迭代器。如列表、元组、字符串、生成器。
迭代器：实现了 __iter__ 和 __next__ 方法。iter() 函数可把可迭代对象转换成迭代器。
为什么生成器省内存？
生成器不把所有值同时存在内存中，只在需要时计算下一个值，适合处理大量数据或无限序列。
"""

lst = [1, 2, 3]
it = iter(lst)       # 获取迭代器
print(next(it))      # 1
print(next(it))      # 2
print(next(it))      # 3
# next(it)           # StopIteration 异常

from collections.abc import Iterable, Iterator

print(isinstance(lst, Iterable))   # True
print(isinstance(lst, Iterator))   # False
print(isinstance(it, Iterator))    # True