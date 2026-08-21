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