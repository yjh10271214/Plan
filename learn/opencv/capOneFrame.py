import cv2

def capOneImg():
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('test.jpg', frame)
            print('摄像头正常，已保存test.jpg')
        else:
            print('摄像头打开但读不到帧')
        cap.release()
    else:
        print('摄像头打不开，检查连接')