# 检测的接口函数
import cv2
import YOLO.mydetect as mydetect # yolo检测
import time
def frametest(frame):
    # frame为帧输入
    # 定义返回变量
    label = []
    labellist=[]
    # # yolo检测
    action = mydetect.predict(frame)
    for labely in action:
         # 在labe加入当前labely
        labellist.append(labely)
    label = labellist
    return label