import numpy as np

#设置随机种子 42
np.random.seed(42)

# 生成二分类数据
N = 200   # 样本数
# 生成两类点：一类在左下，一类在右上
X = np.random.randn(N, 2) # 形状 (N,2)，两个特征
# 根据特征组合生成标签：如果 x0 + x1 > 0 则为 1，否则为 0
y = (X[:, 0] + X[:, 1] > 0).astype(int).reshape(-1, 1) #(N, 1)
# 添加偏置列：X_b 形状 (N,3)
X_b = np.hstack([np.ones((N, 1)), X])    # 第一列全是 1，作为偏置的输入

# 初始化参数
W = np.random.randn(3, 1) * 0.01   # 形状 (3,1)，包含 w0(偏置), w1, w2


# 超参数
learning_rate = 0.1
epochs = 1000

# 定义 sigmoid 函数
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 训练循环
for epoch in range(epochs):
    # 1. 前向传播
    z = X_b @ W  # 形状 (N,1)
    y_pred = sigmoid(z) # 形状 (N,1)

    # 2. 计算二元交叉熵损失
    # 防止 log(0) 出现
    eps = 1e-8
    loss = -np.mean(y * np.log(y_pred + eps) + (1 - y) * np.log(1 - y_pred + eps))

    # 3. 计算梯度
    # 对 z 的梯度
    dz = y_pred - y             # 形状 (N,1)
    # 对 W 的梯度
    grad_W = (1 / N) * X_b.T @ dz   # 形状 (3,1)

    # 4. 更新参数
    W -= learning_rate * grad_W

    # 每 200 轮打印一次
    if (epoch + 1) % 200 == 0:
        print(f"Epoch {epoch+1}, Loss: {loss:.6f}")

# 评估准确率
y_pred_class = (y_pred >= 0.5).astype(int)
accuracy = np.mean(y_pred_class == y)
print(f"训练后准确率: {accuracy:.4f}")
print(f"学习到的参数 W:\n{W}")