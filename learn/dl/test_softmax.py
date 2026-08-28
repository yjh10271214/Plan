import numpy as np

# 设置随机种子 42
np.random.seed(42)

# 生成 3 类数据，每类 100 个点
N_per_class = 100
C = 3
X_list = []
y_list = []

# 类别中心
centers = np.array([[0, 0],
                   [5, 5],
                   [0, 5]])

for i, centers in enumerate(centers):
    X_class = centers + np.random.randn(N_per_class, 2) * 0.8
    y_class = np.full(N_per_class, i) # 标签 0,1,2
    X_list.append(X_class)
    y_list.append(y_class)

X = np.vstack(X_list) # 形状 (300,2)
y = np.hstack(y_list).reshape(-1) # 形状 (300,)

# 加偏置列
X_b = np.hstack([np.ones((len(X), 1)), X])  # 形状 (300,3)

# 初始化权重，形状 (3,3)：3 个输入特征 × 3 个类别
W = np.random.randn(3, C) * 0.01

# 超参数
learning_rate = 0.5
epochs = 1000

# 定义 softmax
def softmax(z):
    z_stable = z - np.max(z, axis=1, keepdims=True) # 减最大值，数值稳定
    exp_z = np.exp(z_stable)
    return exp_z / np.sum(exp_z, axis=1, keepdims=True)

# 将 y 转成 one-hot
y_onehot = np.eye(C)[y] # 形状 (300,3)

for epoch in range(epochs):
    # 1. 前向传播
    z = X_b @ W # 形状 (300,3)
    probs = softmax(z) # 形状 (300,3)

    # 2. 计算交叉熵损失
    eps = 1e-8
    loss = -np.mean(np.sum(y_onehot * np.log(probs + eps), axis=1))

    # 3. 计算梯度
    # 损失对 z 的梯度
    dz = probs - y_onehot # 形状 (300,3)
    # 损失对 W 的梯度
    grad_W = (1 / len(X)) * X_b.T @ dz   # 形状 (3,3)

    # 4. 更新参数
    W -= learning_rate * grad_W

    # 每 200 轮打印
    if (epoch + 1) % 200 == 0:
        print(f"Epoch {epoch+1}, Loss: {loss:.6f}")

# 评估准确率
pred_class = np.argmax(probs, axis=1)   # 取概率最大的类别
accuracy = np.mean(pred_class == y)
print(f"训练后准确率: {accuracy:.4f}")
