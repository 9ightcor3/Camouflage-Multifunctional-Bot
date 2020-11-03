
import cv2   
import numpy as np
import os
import time

import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 

METAL = 26
IN5=23
IN6=24
IN7=25
IN8=8
RED = 2                                  #Associate pin 23 to TRIG
GREEN = 3 
BLUE = 4                                  #Associate pin 23 to TRIG

LASER=17

IN1=21
IN2=20
IN3=16
IN4=12


GPIO.setup(RED,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(GREEN,GPIO.OUT)   
GPIO.setup(BLUE,GPIO.OUT)

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(LASER, GPIO.OUT)

GPIO.output(LASER, False)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO.output(IN1, False)
GPIO.output(IN2, False)
GPIO.output(IN3, False)
GPIO.output(IN4, False)

GPIO.output(RED, False)
GPIO.output(BLUE, False)
GPIO.output(GREEN, False)

##

GPIO.setup(METAL,GPIO.IN)


GPIO.setup(IN5, GPIO.OUT)
GPIO.setup(IN6, GPIO.OUT)
GPIO.setup(IN7, GPIO.OUT)
GPIO.setup(IN8, GPIO.OUT)


GPIO.output(IN5, False)
GPIO.output(IN6, False)
GPIO.output(IN7, False)
GPIO.output(IN8, False)


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)






def DISPOSAL():
    count=0
    while(count<5):
        print('DISPOSAL')
       
        GPIO.output(IN5, True)
        GPIO.output(IN6, False)
        time.sleep(1)
        GPIO.output(IN5, False)
        GPIO.output(IN6, False)
        time.sleep(1)
        GPIO.output(IN5, False)
        GPIO.output(IN6, True)
        time.sleep(1)
        GPIO.output(IN5, False)
        GPIO.output(IN6, False)
        time.sleep(1)
        count +=1

while(1):
    if(GPIO.input(METAL)==False):
      print('BOMB DETECTED')
      DISPOSAL()
