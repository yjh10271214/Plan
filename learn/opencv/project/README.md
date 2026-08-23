# Video Frame Preprocess

## 功能
读取视频文件，逐帧预处理（resize、BGR转RGB、归一化、CHW转换），
每 N 帧保存一张图片，并统计处理耗时。

## 依赖
- numpy
- opencv-python

## 安装
pip install -r requirements.txt

## 使用
python main.py --input test.mp4 --output_dir output_frames --size 640 --save_every 10

## 参数说明
- --input: 视频文件路径（必填）
- --output_dir: 保存图片的目录，默认 output_frames
- --size: resize 目标尺寸，默认 640
- --save_every: 每多少帧保存一张，默认 10

## 输出
- 图片文件: frame_000000.jpg, frame_000010.jpg, ...
- 控制台日志: 显示总帧数、保存帧数、总耗时、平均每帧耗时