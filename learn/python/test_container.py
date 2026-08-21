#容器
# ------------------可变容器-----------------------
# 列表
listDemo = [1, 2, 3, 4]
print(f"列表{listDemo}")
listDemo.append(6)
listDemo[0] = 10

#集合
setDemo = {1, 2, 3, 4}
setDemo.add(6)
setDemo.remove(3)

#字典
dictDemo = {"name": "Time", "age": 20}
dictDemo["sex"] = "female"
del dictDemo["age"]

#字节数组
bytearrayDemo = bytearray(b'hello')
bytearrayDemo[0] = 65

# ------------------不可变容器-----------------------
# 范围
rangeDemo = range(1, 10)
for i in rangeDemo:
    print(i, end = " ")
print("\n")

#字符串
stringDemo = "Irene"
stringDemo = stringDemo.replace('r', 'a')

#元组
tupleDemo = (1, 2, 3, 4)

#字节
bytesDemo = b'Irene'
bytesDemo = bytesDemo.replace(b'r', b'a')

#冻结集合
frozensetDemp = frozenset([1, 2, 3, 4])


