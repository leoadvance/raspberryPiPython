# coding=utf-8
import cv2
import time






if __name__ == "__main__":
    print("start")
    capture = cv2.VideoCapture(1)
    print(capture.isOpened())
    ret, frame = capture.read()
    cv2.imshow("capture", frame)
    # time.sleep(2)
    cv2.imwrite("/tmp/raspberryPiCamera/test.jpeg",frame)
    capture.release()
    print('end')
