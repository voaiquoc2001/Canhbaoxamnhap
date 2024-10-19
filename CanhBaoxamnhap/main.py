import cv2
import numpy as np
from imutils.video import VideoStream
from yolodetect import YoloDetect
import time
from tkinter import messagebox
video = VideoStream(src=1).start()
# Chua cac diem nguoi dung chon de tao da giac
points = []

# new model Yolo
model = YoloDetect()


def handle_left_click(event, x, y, flags, points):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])


def draw_polygon (frame, points):
    for point in points:
        frame = cv2.circle( frame, (point[0], point[1]), 5, (0,0,255), -1)

    frame = cv2.polylines(frame, [np.int32(points)], False, (255,0, 0), thickness=2)
    return frame

detect = False
 
cam =  cv2.VideoCapture(0)

while True:
    ret,frame = cam.read()
    

    # Ve ploygon
    frame = draw_polygon(frame, points)

    if detect:
        frame = model.detect(frame= frame, points= points)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('d'):
        if len (points) ==0:
            messagebox.showerror("Error", "Chưa có điểm nào để nối")
        elif len (points) <= 3:
            messagebox.showerror("Error", "Cần tạo ra ít nhất 4 điểm để tạo ra vùng bảo vệ")
        else:
            points.append(points[0])
            detect = True
    elif key == ord('f'):
        detect = False
    elif key == ord('r'):
        if len (points) == 0:
            messagebox.showerror("Error", "Đã xoá hết điểm, vui lòng kiểm tra lại")
        else:
            points.pop()
    elif key == ord('a'):
        points.clear()
            

    # Hien anh ra man hinh
    cv2.imshow("Intrusion Warning", frame)

    cv2.setMouseCallback('Intrusion Warning', handle_left_click, points)


video.stop()
cv2.destroyAllWindows()