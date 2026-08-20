# 列表推导式
print([x*2 for x in range(5)])
print([x*2 for x in range(5) if x%2==0])

#字典操作
d = {"a":1, "b":2}
print(d["a"])
print(d.get("a"))

name = "tom"
age = 18
s = f"名字:{name}, 年龄:{age}"
print(s)

a1 = [x for x in range(10) if x%2==0]
nums = [1, -2, 3, -4, 5, -6]
a2 = [x for x in nums if (x > 0)]
a3 = [x*x for x in range(1, 11)]
words = ["apple", "hi", "banana", "ok", "cat"]
a4 = [s for s in words if (len(s) > 3)]
a5 = [(i, j) for i in range(2) for j in range(3)]
print('全部偶数:' + str(a1))
print('全部正数:' + str(a2))
print('1-10的平方:' + str(a3))
print('大于3长度的单词:' + str(a4))
print('输出看看:' + str(a5))

d1 = {"name":"张三", "age":20, "gender":"male"}
print(d1)
print(d1.values())
print(d1.get("age", 1))

for k,v in d1.items():
    print(k, v)

words = ["python","java","go"]
nums = [10,20,30]
# enumerate
for i,w in enumerate(words, start=1):
    print(i,w)
# zip
for w,n in zip(words,nums):
    print(w,n)
