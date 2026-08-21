
#异常捕获机制
#raise 主动抛出（触发）异常 
# raise 异常类型("报错描述")
file = None
try:
    file = open('致橡树.txt', 'r', encoding='utf-8')
    print(file.read())
except FileNotFoundError: #except 捕获异常
    print('无法打开指定的文件!')
except LookupError:
    print('指定了未知的编码!')
except UnicodeDecodeError:
    print('读取文件时解码错误!')
finally: #finally 不管异常还是终止，finally里面的都会被执行
    if file:
        file.close()

"""
上下文管理器, 类似c++RAII
"""
with open('致橡树.txt', 'r', encoding='utf-8') as file: #不用手动close
        print(file.read())

#读写二进制文件需要带b, read可以指定
#不是二进制文件，read和write的方法对象是str，二进制文件就是bytes-like(字节串)
try:
    with open('guido.jpg', 'rb') as file1:
        data = file1.read()
    with open('吉多.jpg', 'wb') as file2:
        file2.write(data)
except FileNotFoundError:
    print('指定的文件无法打开.')
except IOError:
    print('读写文件时出现错误.')
print('程序执行结束.')

