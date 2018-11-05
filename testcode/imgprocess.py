#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2 as cv
import numpy as np

#全局阈值
#notice the size of img
def threshold_demo(img):
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #直接阈值化是对输入的单通道矩阵逐像素进行阈值分割。
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    print("threshold value %s"%ret)
    cv.namedWindow("binary0", cv.WINDOW_NORMAL)
    cv.imshow("binary0", binary)

#局部阈值
    #notice the size of img
def local_threshold(img):
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #自适应阈值化能够根据图像不同区域亮度分布，改变阈值
    binary =  cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY, 25, 10)
    cv.namedWindow("binary1", cv.WINDOW_NORMAL)
    cv.imshow("binary1", binary)

#用户自己计算阈值
    
def custom_threshold(img):
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    h, w =gray.shape[:2]
    m = np.reshape(gray, [1,w*h])
    mean = m.sum()/(w*h)
    print("mean:",mean)
    ret, binary =  cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    cv.namedWindow("binary2", cv.WINDOW_NORMAL)
    cv.imshow("binary2", binary)

def test():
  src = cv.imread('/home/pi/project-car/foo.jpg')
  h,w,depth=src.shape
  #notice the resolution, if the pic is so large, the system will reboot
  img=cv.resize(src,(int(w/10),int(h/10)),interpolation=cv.INTER_AREA)
  cv.namedWindow('input_image', cv.WINDOW_NORMAL) #设置为WINDOW_NORMAL可以任意缩放
  cv.imshow('input_image', img)
  threshold_demo(img)
  local_threshold(img)
  custom_threshold(img)
  cv.waitKey(0)
  cv.destroyAllWindows()
