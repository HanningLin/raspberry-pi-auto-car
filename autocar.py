import RPi.GPIO as GPIO
import time
import cv2 as cv
#init para
PIN_1=12#GPIO.1
PIN_4=16#GPIO.4
PIN_5=18#GPIO.5
PIN_6=22#GPIO.6
#init global parameter
FORWARD=70
BACK=30
#FAST
FAST_HIGH=70
SLOW_HIGH=30

#SLOW
FAST_LOW=40
SLOW_LOW=30
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_1,GPIO.OUT)
GPIO.setup(PIN_4,GPIO.OUT)
GPIO.setup(PIN_5,GPIO.OUT)
GPIO.setup(PIN_6,GPIO.OUT)
pin1=GPIO.PWM(PIN_1,50)
pin4=GPIO.PWM(PIN_4,50)
pin5=GPIO.PWM(PIN_5,50)
pin6=GPIO.PWM(PIN_6,50)
pin1.start(0)
pin4.start(0)
pin5.start(0)
pin6.start(0)

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
    
def Forward(sleep_time):
    pin1.ChangeDutyCycle(FORWARD)
    pin4.ChangeDutyCycle(0)
    pin5.ChangeDutyCycle(FORWARD)
    pin6.ChangeDutyCycle(0)
    print("[MOTION]Forward\n")
    time.sleep(sleep_time)
    
def Back(sleep_time):
    pin1.ChangeDutyCycle(0)
    pin4.ChangeDutyCycle(BACK)
    pin5.ChangeDutyCycle(0)
    pin6.ChangeDutyCycle(BACK)
    print("[MOTION]Back\n")
    time.sleep(sleep_time)
    
def RightSlow(sleep_time):
    pin1.ChangeDutyCycle(FAST_LOW)
    pin4.ChangeDutyCycle(0)
    pin5.ChangeDutyCycle(SLOW_LOW)
    pin6.ChangeDutyCycle(0)
    print("[MOTION]RightSlow\n")
    time.sleep(sleep_time)
  
def RightFast(sleep_time):
    pin1.ChangeDutyCycle(FAST_HIGH)
    pin4.ChangeDutyCycle(0)
    pin5.ChangeDutyCycle(SLOW_HIGH)
    pin6.ChangeDutyCycle(0)
    print("[MOTION]RightFast\n")
    time.sleep(sleep_time)

def LeftSlow(sleep_time):
    pin1.ChangeDutyCycle(SLOW_LOW)
    pin4.ChangeDutyCycle(0)
    pin5.ChangeDutyCycle(FAST_LOW)
    pin6.ChangeDutyCycle(0)
    print("[MOTION]LeftSlow\n")
    time.sleep(sleep_time)
    
def LeftFast(sleep_time):
    pin1.ChangeDutyCycle(SLOW_HIGH)
    pin4.ChangeDutyCycle(0)
    pin5.ChangeDutyCycle(FAST_HIGH)
    pin6.ChangeDutyCycle(0)
    print("[MOTION]LeftFast\n")
    time.sleep(sleep_time)

def brake(sleep_time):
    pin1.ChangeDutyCycle(0)
    pin4.ChangeDutyCycle(0)
    pin5.ChangeDutyCycle(0)
    pin6.ChangeDutyCycle(0)
    print("[MOTION]Brake\n")
    time.sleep(sleep_time)  

def main():
    #init parameter
    DELAY=0
    RATIO=0.2
    SLEEP_TIME=0.2
    TURN_THRES=20
    INSIDE_THRESH=1.0/9.0
    element=cv.getStructuringElement(cv.MORPH_CROSS,(5,5))#what for?
    start=time.time()
    cap = cv.VideoCapture(0)
    
    while True:
        #if time.time()-start>20:
         #   break
        ret, frame = cap.read()
        edge=get_edge(frame,RATIO)
        left_edge=edge[0]
        middle_edge=edge[1]
        right_edge=edge[2]
        print("[EDGE]:left{},middle{},right{}".format(left_edge,middle_edge,right_edge))
        diff=left_edge-right_edge
        if(left_edge==0)and(right_edge==0):
            Back(SLEEP_TIME)
            print("[WARNING]edge not found\n")
        elif(left_edge <= middle_edge and middle_edge <=right_edge):#left lower than right, turn right
            if (right_edge >= 480 * RATIO * INSIDE_THRESH):# right is very high
                RightSlow(SLEEP_TIME)
            else:# right low
                RightFast(SLEEP_TIME)
                
        elif(left_edge >= middle_edge and middle_edge >= right_edge):#right lower than left,turn left
            if (right_edge>=480 * RATIO * INSIDE_THRESH):#left very high
                LeftSlow(SLEEP_TIME)
            else:#left low
                LeftFast(SLEEP_TIME)
            
        elif (left_edge>middle_edge and middle_edge<right_edge): #V
            Back(SLEEP_TIME)
        else:#good
            if(diff>TURN_THRES):
                RightSlow(SLEEP_TIME)
            elif(diff<-TURN_THRES):
                LeftSlow(SLEEP_TIME)
            else:
                Forward(SLEEP_TIME)
if __name__ == '__main__':
    main()