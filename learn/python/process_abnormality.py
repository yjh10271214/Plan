try:
    x = int(input("请输入一个数字: "))
    result = 10 / x
    print("结果是:", result)
except ValueError:
    print("输入的不是数字")
except ZeroDivisionError:
    print("不能除以零")
else:
    print("没有异常发生时执行这里")
finally:
    print("无论是否异常都会执行这里")

    # 自动关闭文件，不需要手动 close
with open("test.txt", "w") as f:
    f.write("hello")
# 退出 with 块时，文件自动关闭


class MyError(Exception):
    """自定义异常"""
    pass

def check_age(age):
    if age < 0:
        raise MyError("年龄不能为负数")
    return age

try:
    check_age(-1)
except MyError as e:
    print("发生异常:", e)