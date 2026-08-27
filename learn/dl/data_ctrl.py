import torch

x = torch.arange(12)
print(x)
print(x.shape)
print(x.numel())

x1 = x.reshape(3, 4)
print(x1)
print(x1.shape)
print(x1.numel())
print(torch.zeros((3, 4)))
print(torch.ones((3, 4)))
print(torch.randn(3, 4))
print(torch.tensor([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))

X = torch.arange(12, dtype=torch.float32).reshape((3,4))
Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
torch.cat((X, Y), dim=0), torch.cat((X, Y), dim=1)

#广播机制，形状不同也能加注意隐形的转换

