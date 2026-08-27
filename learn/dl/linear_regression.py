import numpy as np

# 设置随机种子，保证结果可复现
np.random.seed(42)

# 生成模拟数据
# 假设真实关系是 y = 3.5 * x + 1.2 再加上一点噪声
N = 100                    # 样本数
x = np.random.rand(N, 1) * 10   # 输入特征，形状 (N,1)，范围 0~10
true_w = 3.5               # 真实权重
true_b = 1.2               # 真实偏置
noise = np.random.randn(N, 1) * 0.5   # 高斯噪声，标准差 0.5
y = true_w * x + true_b + noise        # 真实标签，形状 (N,1)

# 初始化参数
w = np.random.randn(1, 1)  # 权重，随机初始化为标准正态分布
b = np.zeros((1, 1))       # 偏置，初始化为 0

# 超参数
learning_rate = 0.01       # 学习率
epochs = 500               # 训练轮数

# 记录损失
losses = []

# 训练循环
for epoch in range(epochs):
    # 1. 前向传播：计算预测值
    y_pred = x @ w + b      # 形状 (N,1)

    # 2. 计算损失 MSE
    loss = np.mean((y_pred - y) ** 2)
    losses.append(loss)

    # 3. 计算梯度
    # 损失对 w 的梯度：(2/N) * x.T @ (y_pred - y)
    grad_w = (2 / N) * x.T @ (y_pred - y)
    # 损失对 b 的梯度：(2/N) * sum(y_pred - y)
    grad_b = (2 / N) * np.sum(y_pred - y)

    # 4. 更新参数
    w -= learning_rate * grad_w
    b -= learning_rate * grad_b

    # 每 100 轮打印一次损失
    if (epoch + 1) % 100 == 0:
        print(f"Epoch {epoch+1}, Loss: {loss:.6f}, w: {w[0,0]:.3f}, b: {b[0,0]:.3f}")

# 打印最终结果
print(f"训练后 w: {w[0,0]:.4f}, 真实 w: {true_w}")
print(f"训练后 b: {b[0,0]:.4f}, 真实 b: {true_b}")
print(f"最终 Loss: {loss:.6f}")