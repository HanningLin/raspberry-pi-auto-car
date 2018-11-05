#!/usr/bin/python
# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO
import time

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

def InitGPIO():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(PIN_1,GPIO.OUT)
  GPIO.setup(PIN_4,GPIO.OUT)
  GPIO.setup(PIN_5,GPIO.OUT)
  GPIO.setup(PIN_6,GPIO.OUT)
  
  pin1=GPIO.PWM(PIN_1,FORWARD)
  pin4=GPIO.PWM(PIN_4,FORWARD)
  pin5=GPIO.PWM(PIN_4,FORWARD)
  pin6=GPIO.PWM(PIN_4,FORWARD)
  
def Forward(sleep_time):
  pin1.ChangeDutyCycle(FORWARD)
  pin4.ChangeDutyCycle(0)
  pin5.ChangeDutyCycle(FORWARD)
  pin6.ChangeDutyCycle(0)
  time.sleep(sleep_time)
  
def Back(sleep_time):
  pin1.ChangeDutyCycle(0)
  pin4.ChangeDutyCycle(BACK)
  pin5.ChangeDutyCycle(0)
  pin6.ChangeDutyCycle(BACK)
  time.sleep(sleep_time)
  
def RightSlow(sleep_time):
  pin1.ChangeDutyCycle(FAST_LOW)
  pin4.ChangeDutyCycle(0)
  pin5.ChangeDutyCycle(SLOW_LOW)
  pin6.ChangeDutyCycle(0)
  time.sleep(sleep_time)
  
def RightFast(sleep_time):
  pin1.ChangeDutyCycle(FAST_HIGH)
  pin4.ChangeDutyCycle(0)
  pin5.ChangeDutyCycle(SLOW_HIGH)
  pin6.ChangeDutyCycle(0)
  time.sleep(sleep_time)

def LeftSlow(sleep_time):
  pin1.ChangeDutyCycle(SLOW_LOW)
  pin4.ChangeDutyCycle(0)
  pin5.ChangeDutyCycle(FAST_LOW)
  pin6.ChangeDutyCycle(0)
  time.sleep(sleep_time)
  
def LeftFast(sleep_time):
  pin1.ChangeDutyCycle(SLOW_HIGH)
  pin4.ChangeDutyCycle(0)
  pin5.ChangeDutyCycle(FAST_HIGH)
  pin6.ChangeDutyCycle(0)
  time.sleep(sleep_time)

  
def brake(sleep_time):
  pin1.ChangeDutyCycle(0)
  pin4.ChangeDutyCycle(0)
  pin5.ChangeDutyCycle(0)
  pin6.ChangeDutyCycle(0)
  time.sleep(sleep_time)
  

