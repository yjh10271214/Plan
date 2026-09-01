import numpy as np
import torch
import torch.nn as nn

def conv2d_numpy(x, weight, bias=None, stride=1, padding=0):
    """
    纯 NumPy 实现 conv2d
    
    参数：
    x: 输入，形状 (N, C_in, H, W)
    weight: 卷积核，形状 (C_out, C_in, k, k)
    bias: 偏置，形状 (C_out,)，可选
    stride: 步长，整数
    padding: padding 大小，整数
    
    返回：
    out: 输出，形状 (N, C_out, H_out, W_out)
    """
    N, C_in, H, W = x.shape
    C_out, C_in_w, k, k = weight.shape

    # 断言：输入通道数必须匹配
    assert C_in == C_in_w, f"输入通道 {C_in} 与卷积核通道 {C_in_w} 不匹配"

    # 计算输出尺寸
    H_out = (H + 2 * padding - k) // stride + 1
    W_out = (W + 2 * padding - k) // stride + 1

    # 对输入做 padding
    if padding > 0:
        x_padded = np.pad(
            x,
            ((0, 0), (0, 0), (padding, padding), (padding, padding)),
            mode='constant'
        )
    else:
        x_padded = x
    
    # 初始化输出
    out = np.zeros((N, C_out, H_out, W_out))
    # 遍历每个输出位置
    for n in range(N):
        for c_out in range(C_out):
            for h in range(H_out):
                for w in range(W_out):
                    # 计算滑动窗口位置
                    h_start = h * stride
                    w_start = w * stride
                    
                    # 取出当前窗口：形状 (C_in, k, k)
                    window = x_padded[n, :, h_start:h_start+k, w_start:w_start+k]
                    
                    # 卷积核：形状 (C_in, k, k)
                    kernel = weight[c_out]   # (C_in, k, k)
                    
                    # 计算加权和
                    out[n, c_out, h, w] = np.sum(window * kernel)
            
            # 加偏置
            if bias is not None:
                out[n, c_out, :, :] += bias[c_out]
    
    return out


# 设置随机种子
np.random.seed(42)
torch.manual_seed(42)

# 测试参数
N, C_in, H, W = 2, 3, 6, 6
C_out, k = 4, 3
stride = 2
padding = 1

# 随机输入
x_np = np.random.randn(N, C_in, H, W).astype(np.float32)
weight_np = np.random.randn(C_out, C_in, k, k).astype(np.float32)
bias_np = np.random.randn(C_out).astype(np.float32)

# NumPy 卷积
out_np = conv2d_numpy(x_np, weight_np, bias_np, stride=stride, padding=padding)

# PyTorch 卷积
conv = nn.Conv2d(C_in, C_out, kernel_size=k, stride=stride, padding=padding, bias=True)
with torch.no_grad():
    conv.weight.copy_(torch.from_numpy(weight_np))
    conv.bias.copy_(torch.from_numpy(bias_np))
    out_torch = conv(torch.from_numpy(x_np)).numpy()

# 对比误差
error = np.max(np.abs(out_np - out_torch))
print(f"输出形状: {out_np.shape}")
print(f"最大误差: {error:.8f}")

if error < 1e-5:
    print("✅ 手写 conv2d 与 PyTorch 一致")
else:
    print("❌ 误差过大，需要检查")
