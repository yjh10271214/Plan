import time

class TimingStats:
    """
    统计类，负责计时和记录处理帧数。
    """

    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.total_frames = 0
        self.saved_frames = 0

    def start(self):
        """
        开始计时，记录当前时间。
        """
        # time.time() 返回当前时间戳（从 1970 年至今的秒数）
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    def record_saved(self):
        self.saved_frames += 1

    def report(self):
        """
        生成统计报告。
        
        返回：
        dict: 包含总帧数、保存帧数、总耗时、平均每帧耗时的字典。
        """
        elapsed = self.end_time - self.start_time
        avg_time = elapsed / self.total_frames if self.total_frames > 0 else 0

        return {
            "total_frames": self.total_frames,
            "saved_frames": self.saved_frames,
            "total_time": elapsed,
            "avg_time_per_frame": avg_time,
        }
