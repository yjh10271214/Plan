import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#创建数组对象
array1 = np.array([1, 2, 3, 4])
np.arange(0, 20, 2) #指定范围跨度
np.linspace(-1, 1, 11) #指定范围元素个数生成等差数列
np.logspace(1, 10, num = 10, base = 2) #生成等比数列，base是底数
np.fromstring('1, 2, 3, 4', sep = ',', dtype = 'i8') #从字符串中提取数据创建数组对象
np.random.rand(10) #生成随机数创建数组对象
np.random.randint(1, 100, 10) #生成随机整数创建数组对象
np.random.normal(50, 10, 20) #μ=50 σ=10 随机数 20个
np.random.rand(3, 4) #产生[0,1) 范围的随机小数构成的 3 行 4 列的二维数组
np.random.randint(1, 100, (3, 4, 5)) #[1, 100) 三维
np.zeros((3, 4)) #创建全0、全1或指定元素的数组
np.ones((3, 4))
np.full((3, 4), 10) #指定10
np.eye(4) #单位矩阵


plt.imread('guido.jpg') #读取图片获得对应的三维数组

array1.size #个数
array1.shape #形状
array1.dtype #数据类型
array1.ndim #获得数组维度

#支持切片

 