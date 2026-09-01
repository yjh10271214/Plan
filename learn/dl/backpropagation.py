import numpy as np
from torchvision import datasets, transforms


# 下载 MNIST 数据集
transform = transforms.ToTensor()
train_datatset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)


# 转换成 NumPy 数组
# 训练数据：60000 张 28×28 灰度图，像素值 0~1
X_train = train_datatset.data.numpy().reshape(-1, 784) / 255.0 # (60000, 784)
y_train = train_datatset.targets.numpy()    # (60000,)
X_test = test_dataset.data.numpy().reshape(-1, 784) /255.0  # (10000, 784)
y_test = test_dataset.targets.numpy()   # (10000,)

# 将标签转成 one-hot 编码
def to_onehot(y, num_classes=10):
    """把标签向量转成 one-hot 矩阵"""
    onehot = np.zeros((len(y), num_classes))
    onehot[np.arange(len(y)), y] = 1
    return onehot

y_train_onehot = to_onehot(y_train)
y_test_onehot = to_onehot(y_test)

print(f"训练集: {X_train.shape}, 标签: {y_train_onehot.shape}")
print(f"训练集: {X_test.shape}, 标签: {y_test_onehot.shape}")

def sigmoid(z):
    """sigmoid 激活函数"""
    # 防止 z 太大或太小导致 exp 溢出
    z = np.clip(z, -500, 500) #np.clip(数组, 最小值, 最大值)  ＞500 → 改成 `500`  ＜‑500 → 改成 `-500`
    return 1 / (1 + np.exp(-z))

def sigmoid_derivative(a):
    """sigmoid 导数，输入是 sigmoid 的输出 a"""
    return a * (1 - a)

def softmax(z):
    """softmax 函数，沿 axis=1 计算"""
    # 减去最大值，防止 exp 溢出
    z_stable = z - np.max(z, axis = 1, keepdims=True)
    exp_z = np.exp(z_stable)
    return exp_z / np.sum(exp_z, axis=1, keepdims=True)

def cross_entropy_loss(probs, y_onehot):
    """交叉熵损失"""
    eps = 1e-8
    return -np.mean(np.sum(y_onehot * np.log(probs + eps), axis=1))



# 网络结构
input_size = 784
hidden_size = 128
output_size = 10

# 初始化权重
# 隐藏层权重：用 He 初始化（针对 sigmoid 可以用 Xavier，这里用简单随机小值）
np.random.seed(42)
W1 = np.random.randn(input_size, hidden_size) * 0.01 # (784, 128)
b1 = np.zeros((1, hidden_size)) # (1, 128)
W2 = np.random.randn(hidden_size, output_size) * 0.01    # (128, 10)
b2 = np.zeros((1, output_size)) # (1, 10)


# 超参数
learning_rate = 0.5
epochs = 30
batch_size = 64
N = X_train.shape[0]   # 样本数 60000

# 记录损失和准确率
train_losses = []
test_accuracies = []

for epoch in range(epochs):
    # 打乱数据顺序
    indices = np.random.permutation(N)
    X_shuffled = X_train[indices]
    y_shuffled = y_train_onehot[indices]

    epoch_loss = 0
    num_batches = N // batch_size

    # 小批量训练
    for batch in range(num_batches):
        # 取一个 batch 的数据
        start = batch * batch_size
        end = start + batch_size
        X_batch = X_shuffled[start:end]
        y_batch = y_shuffled[start:end]

        # ---------- 前向传播 ----------
        z1 = X_batch @ W1 + b1  # (64, 128)
        a1 = sigmoid(z1)        # (64, 128)
        z2 = a1 @ W2 + b2       # (64, 10)
        probs = softmax(z2)     # (64, 10)
        
        # ---------- 计算损失 ----------
        loss = cross_entropy_loss(probs, y_batch)
        epoch_loss += loss

        # ---------- 反向传播 ----------
        # 输出层梯度
        dz2 = probs - y_batch   # (64, 10)
        dW2 = a1.T @ dz2 / batch_size   # (128, 10)
        db2 = np.sum(dz2, axis=0, keepdims=True) / batch_size    #(1, 10)

        # 隐藏层梯度
        da1 = dz2 @ W2.T         # (64, 128)
        dz1 = da1 * sigmoid_derivative(a1)  # (64, 128)
        dW1 = X_batch.T @ dz1 / batch_size  # (784, 128)
        db1 = np.sum(dz1, axis=0, keepdims=True) / batch_size   #(1, 128)

        # ---------- 更新参数 ----------
        W1 -= learning_rate * dW1
        b1 -= learning_rate * db1
        W2 -= learning_rate * dW2
        b2 -= learning_rate * db2

    # 每个 epoch 结束后计算平均损失和测试准确率
    avg_loss = epoch_loss / num_batches
    train_losses.append(avg_loss)

    # 评估测试集
    z1_test = X_test @ W1 + b1
    a1_test = sigmoid(z1_test)
    z2_test = a1_test @ W2 + b2
    probs_test = softmax(z2_test)
    pred_test = np.argmax(probs_test, axis=1)
    accuracy = np.mean(pred_test == y_test)
    test_accuracies.append(accuracy)

    print(f"Epoch {epoch+1}/{epochs}, Loss: {avg_loss:.4f}, Test Accuracy: {accuracy:.4f}")

print(f"最终测试准确率: {test_accuracies[-1]:.4f}")


    








