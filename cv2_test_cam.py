# cv2 camera test

from cv2 import VideoCapture, imwrite
cam = VideoCapture(0)
s, img = cam.read()
if s:
    imwrite("camera_test.jpg", img)
