int("10")           # 10
float("3.14")       # 3.14
str(100)            # "100"
list("abc")         # ['a','b','c']
tuple([1,2,3])      # (1,2,3)
dict([("a",1), ("b",2)])  # {'a':1, 'b':2}
set([1,2,2])        # {1,2}
bool(0)             # False
bool(1)             # True


"""
逻辑运算符
"""
a = True
b = False

a and b     # False
a or b      # True
not a       # False

# 短路求值
x = 5
x > 0 and x < 10   # True

# and 和 or 返回的是操作数本身，不一定是布尔值
result1 = 0 or "hello"    # "hello"，因为 0 为假
result2 = 1 and "world"   # "world"，因为 1 为真

"""
in
"""
lst = [1, 2, 3, 4, 5]
2 in lst        # True
10 in lst       # False
10 not in lst   # True

s = "hello"
"h" in s        # True
"x" in s        # False

d = {"name": "Tom", "age": 20}
"name" in d     # True，判断的是键是否存在

"""
身份运算符 is
"""

a = [1, 2, 3]
b = [1, 2, 3]
c = a

a is b       # False，内容相同但对象不同
a is c       # True，同一个对象
a is not b   # True

# 判断 None 必须用 is
x = None
if x is None:
    print("x 是 None")


"""
1. ** 幂运算最高
2. * / // % 高于 + -
3. not > and > or
4. 括号最优先
"""
