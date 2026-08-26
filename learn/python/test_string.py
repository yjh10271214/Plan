s = "Hello, World"

# 常用方法
s.lower()        # 'hello, world' 转小写
s.upper()        # 'HELLO, WORLD' 转大写
s.strip()        # 去首尾空格
s.split(",")     # ['Hello', ' World'] 按逗号分割
s.replace("World", "Python")  # 'Hello, Python' 替换
s.find("World")  # 7，返回下标，找不到返回 -1
s.startswith("H")  # True
s.endswith("d")    # True
s.count("l")       # 3，统计出现次数

# 格式化
name = "Tom"
age = 20
f"{name} is {age} years old"   # f-string 最常用
"{} is {} years old".format(name, age)
"%s is %d years old" % (name, age)