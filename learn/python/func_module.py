import random
import string

ALL_CHARS = string.digits + string.ascii_letters


def generate_code(*, code_len=4):
    """
    生成指定长度的验证码
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码字符串
    """
    return ''.join(random.choices(ALL_CHARS, k=code_len))

for _ in range(5):
    print(generate_code()) 

def is_prime(num: int) -> bool:
    """
    判断一个正整数是不是质数
    :param num: 大于1的正整数
    :return: 如果num是质数返回True，否则返回False
    """
    for i in range(2, int(num ** 0.5) + 1) :
        if num % i == 0:
            return False
    return True

def lcm(x: int, y: int) -> int:
    """求最小公倍数"""
    return x * y // gcd(x, y)

def gcd(x: int, y: int) -> int:
    """求最大公约数"""
    while y % x != 0 :
        x, y = y % x, x
    return x

def calc(*args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = 0
    for item in items:
        if type(item) in (int, float):
            result += item
    return result

def calc(init_value, op_func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item) 
    return result

def add(x, y):
    return x + y

def mul(x, y):
    return x * y

print(calc(0, add, 1, 2, 3, 4, 5, name = '张三'))

import operator
def is_even(num):
    """判断num是不是偶数"""
    return num % 2 == 0
def square(num):
    """求平方"""
    return num ** 2

old_nums = [35, 12, 8, 99, 60, 52]
new_nums = list(map(square, filter(is_even, old_nums)))
print(new_nums)

#偏函数固定一部分参数
import functools

int2 = functools.partial(int, base=2)
int8 = functools.partial(int, base=8)
int16 = functools.partial(int, base=16)

print(int('1001'))    # 1001

print(int2('1001'))   # 9
print(int8('1001'))   # 513
print(int16('1001'))  # 4097

import time
#装饰器
def download(filename):
    """下载文件"""
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')

    
def upload(filename):
    """上传文件"""
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')

download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')

start = time.time()
download('MySQL从删库到跑路.avi')
end = time.time()
print(f'花费时间: {end - start:.2f}秒')
start = time.time()
upload('Python从入门到住院.pdf')
end = time.time()
print(f'花费时间: {end - start:.2f}秒')

def record_time(func):

    def wrapper(*args, **kwargs):
        # 在执行被装饰的函数之前记录开始时间
        start = time.time()
        # 执行被装饰的函数并获取返回值
        result = func(*args, **kwargs)
        # 在执行被装饰的函数之后记录结束时间
        end = time.time()
        # 计算和显示被装饰函数的执行时间
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        # 返回被装饰函数的返回值
        return result
    
    return wrapper

download = record_time(download)
upload = record_time(upload)
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')

@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')


@record_time
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')


from functools import wraps
def record_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        return result
    
    return wrapper

@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')


@record_time
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')


download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
# 取消装饰器的作用不记录执行时间
download.__wrapped__('MySQL必知必会.pdf')
upload.__wrapped__('Python从新手到大师.pdf')


# *args 接收任意数量的位置参数，打包成元组
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3)        # 6
sum_all(1, 2, 3, 4, 5)  # 15

# **kwargs 接收任意数量的关键字参数，打包成字典
def print_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

print_info(name="Tom", age=20)
# name: Tom
# age: 20


def f(a, b, *args, c=10, **kwargs):
    pass

# 顺序必须是：位置参数 → *args → 默认参数 → **kwargs


def f():
    return 1, 2, 3   # 返回元组 (1, 2, 3)

x = f()
print(x)   # (1, 2, 3)

a, b, c = f()   # 解包
print(a, b, c)  # 1 2 3

# 返回 None
def g():
    print("hello")
    # 没有 return 语句，默认返回 None

result = g()   # None


#修改全局变量：global
#嵌套函数修改外层变量：nonlocal
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)   # 20

outer()

#map(func, iterable)：对每个元素应用函数
lst = [1, 2, 3]
result = list(map(lambda x: x**2, lst))
print(result)   # [1, 4, 9]

# 也可以直接写列表推导式，更常用
[x**2 for x in lst]

#filter(func, iterable)：按条件筛选
lst = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, lst))
print(result)   # [2, 4, 6]

# 列表推导式写法
[x for x in lst if x % 2 == 0]

# reduce(func, iterable)：累积计算
from functools import reduce

lst = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, lst)   # 连乘
print(result)   # 120


len()     # 长度
sum()     # 求和
max()     # 最大值
min()     # 最小值
abs()     # 绝对值
round()   # 四舍五入
sorted()  # 排序，返回新列表
enumerate()  # 同时给索引和值
zip()     # 合并多个可迭代对象




