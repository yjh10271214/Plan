# 导入 OpenCV 库
import cv2


def main():
    # -----------------------------
    # 1. 打开摄像头
    # -----------------------------
    # cv2.VideoCapture(0) 表示打开默认摄像头（索引 0）
    # 如果你有多个摄像头，可能需要改成 1 或 2
    cap = cv2.VideoCapture(0)

    # 检查摄像头是否成功打开
    if not cap.isOpened():
        print("无法打开摄像头，请检查连接或尝试修改摄像头索引")
        return

    # -----------------------------
    # 2. 设置摄像头分辨率（可选）
    # -----------------------------
    # 设置宽度
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    # 设置高度
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # 读取实际的分辨率（可能和设置的不完全一样，以实际为准）
    actual_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    actual_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f"摄像头分辨率: {actual_width}x{actual_height}")

    # -----------------------------
    # 3. 设置视频编码器和输出文件
    # -----------------------------
    # fourcc 是视频编码器的四字符代码
    # 'mp4v' 表示 MPEG-4 编码，适合 .mp4 文件
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # 设置帧率，通常摄像头是 30 fps，这里固定 30
    fps = 30.0

    # 创建 VideoWriter 对象，用于写入视频
    # 参数：文件名，编码器，帧率，分辨率
    out = cv2.VideoWriter('test.mp4', fourcc, fps, (actual_width, actual_height))

    # 检查 VideoWriter 是否成功创建
    if not out.isOpened():
        print("无法创建视频文件，请检查编码器或路径")
        cap.release()
        return

    print("开始录制，按 'q' 键停止录制...")

    # -----------------------------
    # 4. 循环读取摄像头帧并写入视频
    # -----------------------------
    while True:
        # 读取一帧
        ret, frame = cap.read()
        if not ret:
            print("读取摄像头失败")
            break

        # 写入视频文件
        out.write(frame)

        # 显示当前画面（可选，在板子上没有 GUI 环境时可能无法显示）
        # 如果不需要显示，可以注释掉下面两行
        # cv2.imshow('Recording', frame)

        # 按 'q' 键退出
        # waitKey(1) 等待 1 毫秒，返回按键的 ASCII 码
        # 注意：在没有 GUI 的环境（比如 SSH 远程）时，cv2.imshow 和 waitKey 可能无法正常工作
        # 如果你是通过 SSH 远程操作，可以注释掉 imshow 和 waitKey 部分，改用定时停止
        # 比如录制固定 100 帧后自动停止

        # 方法一：按 q 停止（需要本地显示窗口）
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # 方法二：录制固定帧数后自动停止（SSH 远程时推荐）
        # 如果你使用 SSH 远程，请注释掉上面的 waitKey 和 imshow，然后取消下面两行注释
        # if frame_count >= 100:  # 录制 100 帧
        #     break

    # -----------------------------
    # 5. 释放资源
    # -----------------------------
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("录制完成，已保存为 test.mp4")


if __name__ == "__main__":
    main()