import numpy as np

class BatchNorm2d:
    def __init__(self, num_features, eps=1e-5, momentum=0.1):
        """
        纯 NumPy 实现 BatchNorm2d
        
        参数：
        num_features: 通道数 C
        eps: 防止除零的小数
        momentum: running 统计量更新动量
        """
        self.num_features = num_features
        self.eps = eps
        self.momentum = momentum

        # 可学习参数
        self.gamma = np.ones((1, num_features, 1, 1))
        self.beta = np.zeros((1, num_features, 1, 1))

        # running 统计量（推理时用）
        self.running_mean = np.zeros((1, num_features, 1, 1))
        self.running_var = np.ones((1, num_features, 1, 1))

        # 训练/推理模式
        self.training = True

    def forward(self, x):
        """
        前向传播
        
        参数：
        x: 输入，形状 (N, C, H, W)
        
        返回：
        y: 输出，形状 (N, C, H, W)
        """
        if self.training:
            # 训练模式：使用当前 batch 的统计量
            # 计算每个通道的均值，形状 (1, C, 1, 1)
            batch_mean = np.mean(x, axis=(0, 2, 3), keepdims=True)
            # 计算每个通道的方差（有偏）
            batch_var = np.var(x, axis=(0, 2, 3), keepdims=True)

            # 归一化
            x_hat = (x - batch_mean) / np.sqrt(batch_var + self.eps)

            # 更新 running 统计量
            self.running_mean = self.momentum * self.running_mean + (1 - self.momentum) * batch_mean
            self.running_var = self.momentum * self.running_var + (1 - self.momentum) * batch_var

        else:
            # 推理模式：使用 running 统计量
            x_hat = (x - self.running_mean) / np.sqrt(self.running_var + self.eps)

        # 缩放和平移
        y = self.gamma * x_hat + self.beta
        return y
    
import torch
import torch.nn as nn

# 随机输入
np.random.seed(42)
torch.manual_seed(42)
x_np = np.random.randn(2, 3, 4, 4).astype(np.float32)

# NumPy 版
bn_np = BatchNorm2d(num_features=3)
bn_np.training = True
y_np = bn_np.forward(x_np)

# PyTorch 版
bn_torch = nn.BatchNorm2d(3)
bn_torch.train()
with torch.no_grad():
    # 设置相同的 gamma 和 beta
    bn_torch.weight.copy_(torch.from_numpy(bn_np.gamma.flatten()))
    bn_torch.bias.copy_(torch.from_numpy(bn_np.beta.flatten()))
    bn_torch.running_mean.copy_(torch.from_numpy(bn_np.running_mean.flatten()))
    bn_torch.running_var.copy_(torch.from_numpy(bn_np.running_var.flatten()))
    y_torch = bn_torch(torch.from_numpy(x_np)).numpy()

# 对比
error = np.max(np.abs(y_np - y_torch))
print(f"输出形状: {y_np.shape}")
print(f"最大误差: {error:.8f}")

if error < 1e-5:
    print("✅ BatchNorm 训练模式实现正确")
else:
    print("❌ 误差过大")