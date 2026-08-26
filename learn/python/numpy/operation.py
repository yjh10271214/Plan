import numpy as np

#矩阵乘法点积
A = np.random.randint(1, 10, size=(2, 2))
B = np.random.randint(1, 10, size=(2, 2))
print(np.dot(A, B))

# @ 是 Python 3.5+ 引入的矩阵乘法运算符
# 本质上等价于 np.dot，但写法更简洁
#推荐：写神经网络代码时，用 @ 更清晰，因为公式里矩阵乘法就是这种形式。
C2 = A @ B
print(C2)

# * 不是矩阵乘法，而是逐元素相乘
C3 = A * B
print("A * B (逐元素):")
print(C3)

x = np.array([0.0, 1.0, 2.0])
print(np.exp(x))
# [1.         2.71828183 7.3890561 ]
# e^0 = 1, e^1 = 2.718..., e^2 = 7.389...


#交叉熵损失函数里会用到 np.log()。
x = np.array([1.0, 2.71828183, 7.3890561])
print(np.log(x))
# [0. 1. 2.]
# ln(1) = 0, ln(e) = 1, ln(e^2) = 2


#注意：np.max() 是求整个数组的最大值，np.maximum() 是逐元素每个对比组取最大，不要混淆
a = np.array([1, 5, 3])
b = np.array([4, 2, 6])
print(np.maximum(a, b))
# [4 5 6]
# 每个位置取两个数组中的较大值

# 也常用于数值稳定性处理
x = np.array([-5, 0, 5])
print(np.maximum(x, 0))
# [0 0 5]  # ReLU 激活函数


#在 BatchNorm 和损失函数统计中，这些会经常用到。
a = np.array([[1, 2, 3],
              [4, 5, 6]])

# np.sum() 求和
print(np.sum(a))           # 21，全部元素相加
print(np.sum(a, axis=0))   # [5 7 9]，沿行方向压缩，每列求和
print(np.sum(a, axis=1))   # [6 15]，沿列方向压缩，每行求和

# np.mean() 求平均
print(np.mean(a))          # 3.5，全部元素平均
print(np.mean(a, axis=0))  # [2.5 3.5 4.5]

# np.std() 求标准差
print(np.std(a))           # 1.7078，全部元素标准差
print(np.std(a, axis=0))   # [1.5 1.5 1.5]

#np.random.seed()：固定随机种子
# 设置随机种子，保证每次运行生成的随机数相同
np.random.seed(42)
print(np.random.rand(3))
# 输出固定，每次运行相同

# 如果不设置种子，每次运行结果不同
print(np.random.rand(3))
# 输出随机，每次运行不同

#为什么需要固定种子？
#在深度学习实验中，为了结果可复现，需要固定随机种子。
#这样别人复现你的代码时，能得到相同的初始权重和数据顺序。


#np.random.randn()：标准正态分布采样
# randn 生成标准正态分布 N(0,1) 的随机数
np.random.seed(42)
a = np.random.randn(3, 2)
print(a)

# 验证均值和标准差
print(np.mean(a)) #接近0
print(np.std(a)) #接近1
#在神经网络权重初始化时，常用 randn 生成高斯分布权重。

# np.random.normal(loc, scale, size)
# loc 是均值，scale 是标准差，size 是形状
a = np.random.normal(0, 0.01, size=(3, 3))
print(a)
# 生成均值 0，标准差 0.01 的 3x3 数组
# 常用于小随机数初始化权重

np.random.seed(42)

# 输入 x：形状 (3, 1)，3 个特征
x = np.random.randn(3, 1)
# 权重 W：形状 (2, 3)，2 个神经元，每个神经元有 3 个权重
W = np.random.randn(2, 3) * 0.01 # 小随机数初始化
# 偏置 b：形状 (2, 1)
b = np.zeros((2, 1))

# 前向传播：z = W @ x + b
z = W @ x + b
print("z = W @ x + b:")
print(z)
print("z.shape:", z.shape)   # (2, 1)

# 应用 ReLU 激活函数：a = max(0, z)
a = np.maximum(z, 0)
print("a = ReLU(z):")
print(a)

# 计算 softmax：先减去最大值（数值稳定性），再 exp，再归一化
z_stable = z - np.max(z)
exp_z = np.exp(z_stable) #取指数
softmax_output = exp_z / np.sum(exp_z, axis=0)
print("softmax 输出:")
print(softmax_output)
print("sum =", np.sum(softmax_output))   # 应该接近 1








