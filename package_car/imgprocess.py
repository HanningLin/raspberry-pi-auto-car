#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2 as cv
import numpy as np
import time
#全局阈值
#notice the size of img
#img e.p.:img = cv.imread('/home/pi/project-car/test_pic/pics/42.jpg')
def get_edge(img):
    h,w,d=img.shape
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #直接阈值化是对输入的单通道矩阵逐像素进行阈值分割。
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    binary_t=binary
    #close
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    closed=cv.morphologyEx(binary,cv.MORPH_CLOSE,kernel);
    opened=cv.morphologyEx(closed,cv.MORPH_OPEN,kernel);#this is the final
    #show pic used to debug
    cv2.imshow("pic", opened)
    cv2.waitKey(1)
    #calcualte the edge
    i = height - 1
    while (i > 0) & (close_opened[i, 0] > 0):
        i -= 1
    left_edge = height - 1 - i
    i = height - 1
    while (i > 0) & (close_opened[i, width - 1] > 0):
        i -= 1
    right_edge = height - 1 - i
    i = height - 1
    while (i > 0) & (close_opened[i, int((width - 1) / 2)] > 0):
        i -= 1
    middle_edge = height - 1 - i
    return [left_edge, middle_edge, right_edge]