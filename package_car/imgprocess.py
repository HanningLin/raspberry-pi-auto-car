#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2 as cv
import time

#全局阈值
#notice the size of img
#img e.p.:img = cv.imread('/home/pi/project-car/test_pic/pics/42.jpg')
def get_edge(img,RATIO):
    h,w,d=img.shape
    h,w=int(h*RATIO),int(w*RATIO)
    frame = cv.resize(img, (w,h))
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #直接阈值化是对输入的单通道矩阵逐像素进行阈值分割。
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    #close
    kernel = cv.getStructuringElement(cv.MORPH_CROSS, (5, 5))
    closed=cv.morphologyEx(binary,cv.MORPH_CLOSE,kernel);
    opened=cv.morphologyEx(closed,cv.MORPH_OPEN,kernel);#this is the final
    #show pic used to debug
    smallpic=cv.resize(opened,(int(w/2),int(h/2)))
    cv.imshow("pic", smallpic)
    cv.waitKey(2)
    #calcualte the edge
    i = h - 1
    while (i > 0) & (opened[i, 0] > 0):
        i -= 1
    left_edge = h - 1 - i
    i = h - 1
    while (i > 0) & (opened[i, w - 1] > 0):
        i -= 1
    right_edge = h - 1 - i
    i = h - 1
    while (i > 0) & (opened[i, int((w - 1) / 2)] > 0):
        i -= 1
    middle_edge = h - 1 - i
    return [left_edge, middle_edge, right_edge]