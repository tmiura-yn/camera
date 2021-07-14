#カメラ映像取得
#接続されているカメラの台数を数える

import cv2
#import datetime

def check_camera_connection():

    capture = cv2.VideoCapture(1)

    while(True):
        ret, frame = capture.read()
        windowsize = (800, 600)
        frame = cv2.resize(frame, windowsize)

        cv2.imshow('title', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): #qを押したら終了
            break
        if cv2.waitKey(1) & 0xFF == ord('s'): #sを押したら保存
            cv2.imwrite('test.jpg',frame)
    capture.release()
    cv2.destroyAllWindows()

"""
        #print("[", datetime.datetime.now(), "]", "searching any camera...")
    true_camera_is = []

    for camera_number in range(0, 10):
        cap = cv2.VideoCapture(camera_number)
        ret, frame = cap.read()

        if ret is True:
            true_camera_is.append(camera_number)
            print("camera_number", camera_number, "Find!")
        else:
            print("camera_number", camera_number, "None")
    print("接続されているカメラは", len(true_camera_is), "台です。")
"""




if __name__ == "__main__":
    check_camera_connection()
