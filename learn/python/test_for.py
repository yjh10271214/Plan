# 遍历列表
lst = [1, 2, 3]
for x in lst:
    print(x)

# 遍历字典的键值对
d = {"name": "Tom", "age": 20}
for k, v in d.items():
    print(k, v)

# 同时获取索引和值
for i, x in enumerate(lst):
    print(i, x)

# 同时遍历多个列表
a = [1, 2, 3]
b = ["x", "y", "z"]
for x, y in zip(a, b):
    print(x, y)

# 用 range 遍历固定次数
for i in range(5):
    print(i)   # 0 1 2 3 4

for i in range(2, 10, 2):
    print(i)   # 2 4 6 8


"""
1.range(start, stop, step) 生成一个序列，不包含 stop。
2.enumerate 同时给索引和值。
3.zip 把多个序列按位置配对。
4.很少用下标循环，直接遍历更 Pythonic。
和 C++ 差异：
1.C++ 常用 for (int i=0; i<n; i++)，Python 用 for i in range(n)。
2.C++ 遍历容器用范围 for for (auto x : v)，Python 写法类似但更灵活。
"""


for i in range(5):
    print(i)
else:
    print("循环正常结束，没有被 break 打断")