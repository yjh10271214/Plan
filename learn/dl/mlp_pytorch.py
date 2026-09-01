import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 设置随机种子，保证结果可复现
torch.manual_seed(42)

#超参数
input_size = 784
hidden_size = 128
num_classes = 10
learning_rate = 0.1
batch_size = 128
epochs = 40

# 数据预处理：转张量，归一化到 [0,1]
transform = transforms.Compose([
    transforms.ToTensor(),  # 转成张量，并自动归一化到 [0,1]
])

# 下载并加载 MNIST 数据集
train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)
# DataLoader：自动分批、打乱、加载数据
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

# 定义 MLP 模型
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        # 第一层：输入 784 -> 隐藏 128
        self.fc1 = nn.Linear(input_size, hidden_size)
        #激活函数
        self.sigmoid = nn.Sigmoid()
        #第二层:隐藏 128 -> 输出 10
        self.fc2 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        # 前向传播
        x = x.view(x.size(0), -1)   # 展平成 (batch_size, 784)
        x = self.fc1(x) # (batch_size, 128)
        x = self.sigmoid(x) # sigmoid 激活
        x = self.fc2(x) # (batch_size, 10)
        return x

# 实例化模型
model = MLP()

# 定义损失函数：交叉熵损失
# 注意：nn.CrossEntropyLoss 内部已经包含 softmax，所以模型前向不需要单独写 softmax
criterion = nn.CrossEntropyLoss()

# 定义优化器：随机梯度下降 SGD
optimizer = optim.SGD(model.parameters(), lr=learning_rate)

# 训练函数
def train():
    model.train()   # 切换到训练模式
    for epoch in range(epochs):
        total_loss = 0
        for images, labels in train_loader:
            # 1. 清空上一轮的梯度
            optimizer.zero_grad()
            # 2. 前向传播
            outputs = model(images)
            # 3. 计算损失
            loss = criterion(outputs, labels)
            # 4. 反向传播：自动计算梯度
            loss.backward()
            # 5. 更新参数
            optimizer.step()
            total_loss += loss.item()

        avg_loss = total_loss / len(train_loader)
        print(f"Epoch {epoch+1}/{epochs}, Loss: {avg_loss:.4f}")

# 测试函数
def evaluate():
    model.eval()   # 切换到评估模式
    correct = 0
    total = 0
    with torch.no_grad():   # 评估时不需要计算梯度
        for images, labels in test_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)   # 取概率最大的类别
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = correct / total
    print(f"Test Accuracy: {accuracy:.4f}")


# 运行训练和测试
train()
evaluate()




