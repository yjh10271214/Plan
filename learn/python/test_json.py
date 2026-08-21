import json

my_dict = {
    'name': '111',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
#将字典格式转化成json字符串
print(json.dumps(my_dict))
#如果要将字典处理成 JSON 格式并写入文本文件，只需要将dumps函数换成dump函数并传入文件对象即可，代码如下所示
with open('data.json', 'w') as file:
    json.dump(my_dict, file)

# json模块有四个比较重要的函数，分别是：
# dump - 将 Python 对象按照 JSON 格式序列化到文件中
# dumps - 将 Python 对象处理成 JSON 格式的字符串
# load - 将文件中的 JSON 数据反序列化成对象
# loads - 将字符串的内容反序列化成 Python 对象

with open('data.json', 'r') as file:
    my_dict = json.load(file)
    print(type(my_dict))
    print(my_dict)




