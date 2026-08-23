import os
import cv2

def save_frame(image_array, save_path):
    """
    将预处理后的张量保存为图片。
    
    参数：
    image_array: 预处理后的图像，形状 (1, C, H, W)，RGB 格式，float32 类型，值范围 0~1
    save_path: 保存图片的完整路径，比如 "output_frames/frame_000000.jpg"
    """

    # 1. 去掉 batch 维
    # image_array[0] 取出第 0 个 batch，形状从 (1, C, H, W) 变成 (C, H, W)
    img = image_array[0]

    # 2. 维度转换：CHW 转 HWC
    # 把形状从 (C, H, W) 转回 (H, W, C)
    # 这是第 4 步的反向操作
    img = img.transpose(1, 2, 0)

    # 4. 颜色空间转换：RGB 转 BGR
    # 因为 OpenCV 保存图片时默认按 BGR 顺序处理
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # 5. 确保保存目录存在
    # os.path.dirname(save_path) 获取 save_path 中的目录部分
    # os.makedirs(..., exist_ok=True) 创建目录，如果已存在不报错
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # 6. 保存图片
    # cv2.imwrite 的第一个参数是文件路径，第二个参数是图像数据
    cv2.imwrite(save_path, img)