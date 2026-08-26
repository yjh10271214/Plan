# 普通函数
def add(a, b):
    return a + b

# lambda 写法
add = lambda a, b: a + b

print(add(1, 2))   # 3

# 常用场景：作为参数传给排序等函数
students = [("Tom", 90), ("Jerry", 80), ("Alice", 95)]
students.sort(key=lambda x: x[1])  # 按分数排序
print(students)