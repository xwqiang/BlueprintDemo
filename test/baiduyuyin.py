# created by Huang Lu
# 27/08/2016 17:05:45
# Department of EE, Tsinghua Univ.

import cv2
import numpy as np

def test():
    cap = cv2.VideoCapture(0)
    while(1):
        # get a frame
        ret, frame = cap.read()
        # show a frame
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()



def test1():
    import os
    import numpy
    from PIL import Image, ImageDraw
    import cv2

    cap = cv2.VideoCapture(0)
    # fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    # fourcc = cv2.CAP_PROP_FOURCC('I', '4', '2', '0')
    video = cv2.VideoWriter("~/Downloads/aaa.avi", cv2.CAP_PROP_FOURCC, 5, size)
    print( cap.isOpened())

    classifier = cv2.CascadeClassifier("~/Downloads/haarcascade_frontalface_alt.xml")

    count = 0
    while count > -1:
        ret, img = cap.read()
        faceRects = classifier.detectMultiScale(img, 1.2, 2, cv2.CASCADE_SCALE_IMAGE, size)
        if len(faceRects) > 0:
            for faceRect in faceRects:
                x, y, w, h = faceRect
                cv2.rectangle(img, (int(x), int(y)), (int(x) + int(w), int(y) + int(h)), (0, 255, 0), 2, 0)
        video.write(img)
        cv2.imshow('video', img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    video.release()
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test1()