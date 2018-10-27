import RPi.GPIO as GPIO
import time

PIN_1=12#GPIO.1
PIN_4=16#GPIO.4
PIN_5=18#GPIO.5
PIN_6=22#GPIO.6


def init():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(PIN_1,GPIO.OUT)
  GPIO.setup(PIN_4,GPIO.OUT)
  GPIO.setup(PIN_5,GPIO.OUT)
  GPIO.setup(PIN_6,GPIO.OUT)
def forward(sleep_time):
  init() 
  GPIO.output(PIN_1,GPIO.HIGH)
  GPIO.output(PIN_4,False)
  GPIO.output(PIN_5,GPIO.HIGH)
  GPIO.output(PIN_6,False)
  time.sleep(sleep_time)
  GPIO.cleanup()
def back(sleep_time):
  print('back')
  init() 
  GPIO.output(PIN_1,False)
  GPIO.output(PIN_4,GPIO.HIGH)
  GPIO.output(PIN_5,False)
  GPIO.output(PIN_6,GPIO.HIGH)
  time.sleep(sleep_time)
  GPIO.cleanup()
def left(sleep_time):
  init() 
  GPIO.output(PIN_1,False)
  GPIO.output(PIN_4,GPIO.HIGH)
  GPIO.output(PIN_5,GPIO.HIGH)
  GPIO.output(PIN_6,False)
  time.sleep(sleep_time)
  GPIO.cleanup()
def right(sleep_time):
  init() 
  GPIO.output(PIN_1,GPIO.HIGH)
  GPIO.output(PIN_4,False)
  GPIO.output(PIN_5,False)
  GPIO.output(PIN_6,GPIO.HIGH)
  time.sleep(sleep_time)
  GPIO.cleanup()
def brake(sleep_time):
  init() 
  GPIO.output(PIN_1,False)
  GPIO.output(PIN_4,False)
  GPIO.output(PIN_5,False)
  GPIO.output(PIN_6,False)
  time.sleep(sleep_time)
  GPIO.cleanup()

print('F')
forward(3)
print('B')
back(3)
print('L')
left(3)
print('B')
brake(3)
print('R')
right(3)

