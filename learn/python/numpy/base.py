import numpy as np

a = np.array([1, 2, 3])
print(a)
print(a.dtype)


b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b.dtype)


c = np.array([1, 2, 3], dtype=np.float32)
print(c)
print(c.dtype)


#第一个参数是形状元组 (rows, cols)，dtype 指定类型，默认 float64。
a = np.zeros((1,2))
print(a)
b = np.zeros((1,2), dtype=np.int32)
print(b.dtype)

a = np.ones((3, 2))
print(a)

# 0 到 9
a = np.arange(10)
print(a)

 # 起始 2，结束 10（不包含），步长 2
b = np.arange(2, 10, 2)
print(b)

c = np.arange(5, dtype=np.float32)
print(c)
c = np.arange(5, dtype=np.uint8)
print(c)

# 从 0 到 1，取 5 个点，包含端点 
a = np.linspace(0, 1, num=5)
print(a)
#参数：start、stop、num（个数），默认包含 stop；endpoint=False 则不包含。
b = np.linspace(0, 1, num=5, endpoint=False)
print(b)


# 形状 (3,2)，值在 [0,1)
#np.random.rand(d0, d1, ...)：生成 [0,1) 均匀分布的浮点数
a = np.random.rand(3, 2)
print(a)


#参数：low 包含，high 不包含；size 可指定形状，不指定则返回标量或一维数组。
#np.random.randint(low, high=None, size=None)：生成指定范围的随机整数
print(np.random.randint(0, 10, size=(2,3)))
# 0~4 整数，一维 5 个
print(np.random.randint(5, size=5))


#数组属性
a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int16)
print(a.shape)  # (2, 3)  形状元组
print(a.ndim)   # 2       维度数 number‑of‑dimensions
print(a.size)   # 6       元素总数
print(a.dtype)  # int16   数据类型
print(a.itemsize) # 2       每个元素字节数（int16 占 2 字节）

#改变数组形状，但元素总数不变。
a = np.arange(12)          # [0 1 2 ... 11]
b = a.reshape(3, 4)        # 变成 3 行 4 列
print(b)

#关键：-1 是自动推导维度，常用于不确定某一维大小时。
c = a.reshape(2, -1) # -1 表示自动推断，2 行，列数自动算
print(c)


#都是将多维数组展平成一维。 
#flatten() 返回拷贝，修改不影响原数组。 压扁、摊平
#ravel() 返回视图（如果可能），修改会影响原数组。 拆散、解开缠绕
a = np.array([[1, 2], [3, 4]])
b = a.flatten()
c = a.ravel()
print(b)  # [1 2 3 4]
print(c)  # [1 2 3 4]

#基础索引与切片
a = np.array([10, 20, 30, 40, 50])
print(a[0])      # 10
print(a[1:4])    # [20 30 40]
print(a[::-1])   # [50 40 30 20 10]  反转

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(a[0, 1])       # 2
print(a[0])          # [1 2 3]  第0行
print(a[:, 0])       # [1 4 7]  第0列
print(a[:2, 1:])     # [[2 3]
                     #  [5 6]]

a = np.random.rand(2, 3, 4)   # 形状 (2,3,4)
print(a[0].shape)             # (3,4)
print(a[0, 1].shape)          # (4,)
print(a[0, 1, 2])             # 标量


#用条件表达式筛选元素。
#布尔索引
a = np.array([10, 20, 30, 40, 50])
mask = a > 25
print(mask)
print(a[mask])

print(a[a > 25])     # [30 40 50]


a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(a[a > 5])

#花式索引
#用整数数组或列表指定位置。
a = np.array([10, 20, 30, 40, 50])
idx = [0, 2, 4]
print(a[idx])   # [10 30 50]

# 二维：取指定行
a = np.arange(12).reshape(3, 4)
print(a[[0, 2]]) # 取第0行和第2行


# 练习1：用 np.array 创建一维数组 [1,2,3,4,5] 并打印
print(np.array([1,2,3,4,5]))
# 练习2：用 np.zeros 创建 3x3 全 0 数组，打印其 dtype
a = np.zeros((3, 3))
print(a.dtype)
# 练习3：用 np.ones 创建 2x4 全 1 数组，打印 shape
print(np.ones((2, 4)).shape)
# 练习4：用 np.arange 创建 0 到 9 的数组，并 reshape 成 2x5
print(np.arange(0, 10).reshape(2, 5))
# 练习5：用 np.linspace 创建 0 到 1 之间 11 个点
print(np.linspace(0, 1, num=11))
# 练习6：用 np.random.rand 创建 4x3 随机数组，打印 ndim 和 size
a = np.random.rand(4, 3)
print(a.ndim)
print(a.size)
# 练习7：创建一个 3x3 数组，用整数索引取出第 1 行第 2 列的元素
a = np.random.randint(9, size=(3, 3))
print(a)
print(a[0, 1])
print(a[:, 1:2])
# 练习8：用布尔索引从 np.array([1,5,10,15,20]) 中选出大于 10 的元素
a = np.array([1,5,10,15,20])
mask = a > 10
print(a[mask])
print(a[a > 10])
# 练习9：用花式索引从一维数组 [10,20,30,40,50] 中取出第 0 和第 3 个元素
a = np.array([10,20,30,40,50])
idx = [0, 3]
print(a[idx])
# 练习10：创建一个 3x4 数组，使用 reshape 变成 4x3，再 flatten 成一维，打印所有结果
a = np.zeros((3, 4)).reshape(4, 3)
a = np.random.randint(0, 12, size=(3, 4))
print(a)
a = a.reshape(4, 3)
print(a)
a = a.flatten()
print(a)











