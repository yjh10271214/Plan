import os
import argparse
import logging
from video_source import VideoSource          # 从 video_source.py 导入 VideoSource 类
from preprocess import preprocess_frame      # 从 preprocess.py 导入 preprocess_frame 函数
from storage import save_frame               # 从 storage.py 导入 save_frame 函数
from stats import TimingStats                # 从 stats.py 导入 TimingStats 类


def parse_args():
    # argparse.ArgumentParser 用于解析命令行参数
    parser = argparse.ArgumentParser(description="视频逐帧预处理程序")
    parser.add_argument("--input", type=str, required=True, help="输入视频路径")
    parser.add_argument("--output_dir", type=str, default="output_frames", help="保存图片的目录")
    parser.add_argument("--size", type=int, default=640, help="目标尺寸")
    parser.add_argument("--save_every", type=int, default=10, help="每多少帧保存一张")

     # 解析参数并返回
    return parser.parse_args()


def main():

    # 配置日志
    # level=logging.INFO 表示输出 INFO 及以上级别的日志
    # format 定义日志格式：时间 - 级别 - 消息
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    args = parse_args() # 解析命令行参数

    if not os.path.exists(args.input):
        logging.error(f"video file absent: {args.input}")
        raise SystemExit(1)

    os.makedirs(args.output_dir, exist_ok=True) # 创建输出目录（如果不存在）
    # 初始化视频源
    source = VideoSource(args.input) 
    # 初始化统计对象，并设置总帧数
    stats = TimingStats()
    stats.total_frames = source.total_frames

    # 输出视频信息
    logging.info(f"video info: {source.width}x{source.height}, {source.fps} fps, {source.total_frames} 帧")
    logging.info(f"save strategy: each {args.save_every} frame save a image")

    stats.start()

    frame_idx = 0
    while True:
        frame = source.read_frame()
        if frame is None:
            break
        
        processed = preprocess_frame(frame, (args.size, args.size))

        if frame_idx % args.save_every == 0:
            # 构造保存路径：output_dir/frame_000000.jpg
            save_path = os.path.join(args.output_dir, f"frame_{frame_idx:06d}.jpg")
            save_frame(processed, save_path)
            stats.record_saved()

        frame_idx += 1

        # 每处理 100 帧打印一次进度
        if frame_idx % 100 == 0:
            logging.info(f"processed {frame_idx} / {source.total_frames} frames")

    stats.stop()
    source.release()
    report = stats.report()

    logging.info(f"processed successfully: total {report['total_frames']} frames, save {report['saved_frames']} frames")
    logging.info(f"total take up times: {report['total_time']:.3f} s")
    logging.info(f"average: {report['avg_time_per_frame']*1000:.2f} ms")


if __name__ == "__main__":
    main()

