import numpy as np

A = np.array([[1, 2], [3, 4]])
print(f"A   shape:{A.shape}, size:{A.size}")
B = np.array([[5, 6], [7, 8]])
print(f"B   shape:{B.shape}, size:{B.size}")
print(A @ B) # @ 矩阵乘法

import torch
import torch.nn.functional as F
#随机logits
z = torch.tensor([2.0, 1.0, 0.1], requires_grad=True)
#真实标签(类别0)
y_true = torch.tensor([1.0, 0.0, 0.0])

#计算 softmax 交叉熵损失
p = F.softmax(z, dim=0)
loss = -torch.sum(y_true * torch.log(p))

#方向传播
loss.backward()

print("p = ", p)
print("z.grad = ", z.grad)
print("p - y_true = ", p - y_true)

# ====================== 导入依赖包 ======================
# 导入pytorch核心库，张量创建、运算、自动求导全部依赖它
import torch
# nn 全称 neural network，存放神经网络层、损失函数（CrossEntropyLoss 在这个包里）
import torch.nn as nn
# F 是functional，存放纯运算函数（softmax、log_softmax），不需要创建实例直接调用
import torch.nn.functional as F

# ====================== 1. 定义网络原始输出 logits ======================
# torch.tensor()：创建PyTorch专用数组【张量tensor】，支持自动微分
# 外层 []：batch维度，代表一批里面有 1 条样本（batch_size=1）
# 内层 [3.0, 1.0, 0.0]：3分类原始打分logits，可正可负，还不是概率
# 整体形状 [1, 3] 含义：[样本数量, 类别总数]
logits = torch.tensor([[3.0, 1.0, 0.0]])  

# ====================== 2. 手动执行softmax，查看转化后的预测概率 ======================
# F.softmax()：执行softmax运算，把logits转换成合法概率分布
# dim=1：沿着第1维度做指数求和归一化（对每条样本内部的各个类别求和，保证一行概率总和=1）
p = F.softmax(logits, dim=1)
print("softmax 输出各类预测概率 p：")
print(p)

# ====================== 3. 定义真实标签 ======================
# 这条样本真实类别是第0类，框架CrossEntropyLoss直接接收类别索引，不用手写one-hot
label = torch.tensor([0])  

# ====================== 4. 定义交叉熵损失函数 ======================
# nn.CrossEntropyLoss()：交叉熵损失【内部自带softmax运算】
# ⚠️重点：输入必须是原始logits，不能提前手动softmax！
loss_fn = nn.CrossEntropyLoss()
# 传入原始打分logits + 真实标签，自动完成softmax+交叉熵计算
loss = loss_fn(logits, label)
print("\n交叉熵损失 loss =", loss.item())

# ====================== 5. 手动拆分 softmax + 交叉熵，用来和上面结果对照验证 ======================
# F.log_softmax：先softmax，再取对数，等价 log(softmax(logits))
log_p = F.log_softmax(logits, dim=1)
# NLLLoss：接收 log(softmax) 的结果计算损失，组合起来 = CrossEntropyLoss
loss_manual = nn.NLLLoss()(log_p, label)
print("手动 softmax+交叉熵 loss =", loss_manual.item())

# ====================== 6. 开启自动求导，反向传播计算梯度 ======================
# requires_grad=True：标记这个张量需要记录运算链路，后续可以求导
logits.requires_grad = True  
# 重新计算损失（现在logits开启了求导记录）
loss = loss_fn(logits, label)
# loss.backward()：反向传播，链式法则自动算出 dL/dz 梯度，存入logits.grad
loss.backward()
print("\ndL/dz 梯度：")
print(logits.grad)


import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader


# 1. 准备数据
transform = transforms.ToTensor() # 把图片转成张量，并归一化到 [0,1]
train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset  = datasets.MNIST(root='./data', train=False, download=True, transform=transform)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader  = DataLoader(test_dataset, batch_size=64, shuffle=False)

# 2. 定义模型：单层全连接，输入 28*28=784，输出 10 个类别
class SoftmaxRegression(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(784, 10)  # 线性层，对应 z = Wx + b

    def forward(self, x):
        x = x.view(x.size(0), -1)    # 把图片展平成一维向量
        z = self.fc(x)                # 线性变换
        return z                      # 返回 logits，不用手动 softmax

model = SoftmaxRegression()

# 3. 定义损失函数（内部包含 softmax + 交叉熵）
criterion = nn.CrossEntropyLoss()

# 4. 定义优化器：随机梯度下降
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 5. 训练循环
for epoch in range(5):
    total_loss = 0
    for images, labels in train_loader:
        # 前向传播
        logits = model(images)
        loss = criterion(logits, labels)

        # 反向传播
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f'Epoch {epoch+1}, Loss: {total_loss/len(train_loader):.4f}')




