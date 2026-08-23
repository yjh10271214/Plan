import cv2
import numpy as np

def preprocess_frame(frame, input_size=(640, 640)):
    """
    对视频帧进行预处理，转换为模型输入需要的格式。
    
    参数：
    frame: 输入帧，形状 (H, W, C)，BGR 格式，uint8 类型
    input_size: 目标尺寸，是一个元组 (宽, 高)，默认 (640, 640)
    
    返回：
    img: 预处理后的图像，形状 (1, C, H, W)，RGB 格式，float32 类型
         - 1 表示 batch 维度
         - C 表示通道数，这里固定为 3
         - H, W 分别是高和宽
    """
    # 1. resize：把图像缩放到目标尺寸
    img = cv2.resize(frame, input_size)
    # 2. 颜色空间转换：BGR 转 RGB
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    # 3. 归一化：把像素值从 0~255 映射到 0~1 之间
    img = img.astype(np.float32) / 255.0
    # 4. 维度转换：HWC 转 CHW
    # 原始 img 形状是 (H, W, C)，即 (高, 宽, 通道)
    # 深度学习模型通常需要 (C, H, W)，即 (通道, 高, 宽)
    img = img.transpose(2, 0, 1)

    # 5. 增加 batch 维度
    # np.expand_dims(img, axis=0) 在第一个位置增加一个维度
    img = np.expand_dims(img, axis=0)

    return img