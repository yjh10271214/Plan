"""
负责打开视频文件，逐帧读取:
1.用 cv2.VideoCapture 打开视频
2.检查是否成功打开
3.提供 read_frame() 方法返回下一帧
4.获取视频信息(总帧数、FPS、尺寸)
"""
import cv2

class VideoSource:
    def __init__(self, video_path):
        # cv2.VideoCapture 用于打开视频文件或摄像头
        self.cap = cv2.VideoCapture(video_path) #如果传入路径，就是打开视频文件；如果传入 0，就是打开摄像头
        if not self.cap.isOpened():
            raise FileNotFoundError(f"invalid open video file: {video_path}")
        self.total_frames = self.cap.get(cv2.CAP_PROP_FRAME_COUNT) # cv2.CAP_PROP_FRAME_COUNT 是 OpenCV 内置属性，表示视频的总帧数
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)  # 获取视频帧率（FPS，每秒多少帧）
        # 获取视频的宽度和高度
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def read_frame(self):
        """
        读取下一帧。
        
        返回：
        frame: 下一帧图像，形状 (H, W, C), BGR 格式, uint8 类型。
               如果视频读完，返回 None。
        """
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def release(self):
        self.cap.release()



