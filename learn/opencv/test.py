import cv2
import numpy as np

#读出来的是一个numpy数组, dtype 默认是 uint8，范围 0~255
img = cv2.imread("test.jpg")
print(img.shape)    #shape出来的是(H,W,C)

#resize 指定大小是(W, H)和shape相反
img = cv2.resize(img, (640, 640))   
print(img.shape)    

#OpenCV 读进来是 BGR 顺序，但深度学习模型通常用 RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #这一步本质上是交换了通道顺序
# img = img[:, :, ::-1] #逆序第三维

#归一化到[0,1]
"""
astype(np.float32) 把数据类型从 uint8 转成 float32
除以 255.0 把像素值从 0~255 归一化到 0.0~1.0
这是深度学习的标准做法，因为模型训练时输入通常是 0~1 之间的浮点数
"""
img = img.astype(np.float32) / 255.0

"""
5. HWC 转 CHW
当前 shape 是 (H, W, C)，即 (640, 640, 3)。
但 PyTorch 等框架要求输入是 (C, H, W)，即通道维在最前面。
原来的维度顺序是 (0, 1, 2) 对应 (H, W, C)。
transpose(2, 0, 1)
"""
img = img.transpose(2, 0, 1)

"""
6. 加 batch 维
模型推理通常输入是一个 batch,形状是 (N, C, H, W)，即使单张图也要加一个 batch 维度
"""
img = np.expand_dims(img, axis=0)
# 或者 img = img.reshape(1, 3, 640, 640)
print(img.shape)
