import time
import numpy as np

def record_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} execute time: {end_time - start_time:.2f}")
        return result

    return wrapper

@record_time
def matmul_python(A, B):
    """
    纯 Python 实现矩阵乘法 C = A × B
    
    参数：
    A: 二维列表，形状为 (n, k)
    B: 二维列表，形状为 (k, m)
    
    返回：
    C: 二维列表，形状为 (n, m)
    """
    n = len(A) #获取行数
    m = len(B[0]) #获取列数
    k = len(B)
    # 创建结果矩阵 C，初始化为 n 行 m 列的全 0 矩阵
    # 列表推导式：[0.0] * m 生成一行 m 个 0，外层循环 n 次生成 n 行
    C = [[0.0] * m for _ in range(n)]
    for i in range(n): #遍历A的n行
        for j in range(m):  #遍历B的m列
            s = 0.0
            for p in range(k):
                s += A[i][p]*B[p][j]

            C[i][j] = s
    
    return C;

n = 200
A = [[i + j for j in range(n)] for i in range(n)]
B = [[i - j for j in range(n)] for i in range(n)]
matmul_python(A, B)
# print(matmul_python(A, B))


A_np = np.arange(n*n, dtype=np.float64).reshape(n, n)
B_np = np.arange(n*n, dtype=np.float64).reshape(n, n)
dot_time = record_time(np.dot)
C_np = dot_time(A_np, B_np)
# print(C_np)
"""
    numpy为什么快：
    原因1：向量化（SIMD 指令）
    因为NumPy 调用的是 BLAS 库（基本线性代数子程序库），它利用了 CPU 的 SIMD 指令集。
    SIMD 是什么？
    全称 Single Instruction Multiple Data，单指令多数据。
    条指令同时处理 4、8、16 个数据。
    所以同样的计算量，NumPy 用 1 条指令完成了纯 Python 需要 16 次循环才能做的事。
    速度提升：十几倍甚至几十倍。


    原因2：连续内存布局
    Python 列表是指针数组，每个元素是一个独立的对象，分散在内存各处。
    内存非常分散
    访问 A[i][j] 需要多次指针跳转
    CPU 缓存命中率极低

    NumPy 数组的内存结构 NumPy 数组是一块连续的内存块，所有元素紧挨着存储。
    也就是说，A[0][1] 和 A[0][2] 在物理内存上是相邻的。
    CPU 访问内存时，会一次加载一整块到缓存（cache line，通常 64 字节）。
    连续内存意味着：
    一次加载就能取到很多需要的数据
    缓存命中率高
    不需要频繁从主存取数
    可以类比 C 数组和链表遍历的速度差异。

    
    原因3：消除 Python 解释器开销
    每执行一次 A[i][p] * B[p][j]，Python 解释器要做：
    类型检查：A[i][p] 是 int 吗？
    边界检查：i 和 p 是否越界？
    指针解引用：通过多级指针找到实际数据
    装箱/拆箱：Python int 是对象，运算时要拆出底层 C long，算完再装回 Python int 对象
    创建新对象：每次 s += ... 都会创建新的 Python int 对象，旧对象交给垃圾回收器
    每一次循环迭代，都有几十条额外的 Python 虚拟机指令。

    NumPy 怎么做？
    NumPy 的循环在 C 层执行，没有 Python 解释器参与。
    没有类型检查：C 代码里类型是固定的
    没有边界检查：循环范围已经确定
    没有装箱/拆箱：直接是 C double 运算
    没有对象创建：直接在内存缓冲区累加
    速度提升：几十倍。

    原因4：多线程并行
    大型 NumPy 运算（比如矩阵乘法）会调用 BLAS 库，比如 OpenBLAS、MKL。
    这些库在编译时就已经优化好，并且支持多线程并行。
    当你做 np.dot(A, B) 时，如果矩阵够大，OpenBLAS 会自动把任务分给多个 CPU 核心同时计算。
    纯 Python 的 for 循环只能用一个核心，无法并行。
    速度提升：核心数倍。
    例如 4 核 CPU，理论上最多再快 4 倍。
"""




