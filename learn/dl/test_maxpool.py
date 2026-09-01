import numpy as np

def maxpool2d_numpy(x, kernel_size=2, stride=2, padding=0):
    """
    纯 NumPy 实现 maxpool2d
    
    参数：
    x: 输入，形状 (N, C, H, W)
    kernel_size: 池化窗口大小，整数
    stride: 步长
    padding: 填充大小
    
    返回：
    out: 输出，形状 (N, C, H_out, W_out)
    """
    N, C, H, W = x.shape
    k = kernel_size

    # 计算输出尺寸
    H_out = (H + 2 * padding - k) // stride + 1
    W_out = (W + 2 * padding - k) // stride + 1

    # 对输入做 padding
    # 注意：maxpool 的 padding 通常补 -inf，这样不会影响 max 取值
    # 但这里为了简单，我们直接忽略 padding，只支持 padding=0
    if padding > 0:
        x_padded = np.pad(
            x,
            ((0, 0), (0, 0), (padding, padding), (padding, padding)),
            mode='constant',
            constant_values=-np.inf
        )
    else:
        x_padded = x

    # 初始化输出
    out = np.zeros((N, C, H_out, W_out))

    # 遍历每个输出位置
    for n in range(N):
        for c in range(C):
            for h in range(H_out):
                for w in range(W_out):
                    h_start = h * stride
                    w_start = w * stride

                    # 取出当前窗口
                    window = x_padded[n, c, h_start:h_start+k, w_start:w_start+k]

                    # 取最大值
                    out[n, c, h, w] = np.max(window)

    return out

import torch
import torch.nn as nn

# 随机输入
np.random.seed(42)
x_np = np.random.randn(2, 3, 6, 6).astype(np.float32)

# NumPy 版
out_np = maxpool2d_numpy(x_np, kernel_size=2, stride=2, padding=0)

# PyTorch 版
maxpool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
out_torch = maxpool(torch.from_numpy(x_np)).numpy()

# 对比
error = np.max(np.abs(out_np - out_torch))
print(f"输出形状: {out_np.shape}")
print(f"最大误差: {error:.8f}")

if error < 1e-5:
    print("✅ maxpool 实现正确")
else:
    print("❌ 误差过大")