import cv2   
import numpy as np
import os
import time

import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 


RED = 2                                  #Associate pin 23 to TRIG
GREEN = 3 
BLUE = 4                                  #Associate pin 23 to TRIG


IN5=25
IN6=8
IN7=23
IN8=24
                                #Associate pin 23 to TRIG


IN1=20
IN2=21
IN3=16
IN4=12


GPIO.setup(IN5, GPIO.OUT)
GPIO.setup(IN6, GPIO.OUT)
GPIO.setup(IN7, GPIO.OUT)
GPIO.setup(IN8, GPIO.OUT)


GPIO.setup(RED,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(GREEN,GPIO.OUT)   
GPIO.setup(BLUE,GPIO.OUT)

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)



GPIO.output(IN1, False)
GPIO.output(IN2, False)
GPIO.output(IN3, False)
GPIO.output(IN4, False)

GPIO.output(IN5, False)
GPIO.output(IN6, False)
GPIO.output(IN7, False)
GPIO.output(IN8, False)


GPIO.output(RED, False)
GPIO.output(BLUE, False)
GPIO.output(GREEN, False)




GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)






def motor1():
    print('111')
   
    GPIO.output(IN5, True)
    GPIO.output(IN6, False)
    time.sleep(1)
    GPIO.output(IN5, False)
    GPIO.output(IN6, False)
    time.sleep(1)

def motor2():
    count=0
    while(count<5):
        print('2222')
       
        GPIO.output(IN7, True)
        GPIO.output(IN8, False)
        time.sleep(1)
        GPIO.output(IN7, False)
        GPIO.output(IN8, False)
        time.sleep(1)
        count +=1

while(1):
    
      print('checking')
      motor2()
      time.sleep(1)
##      motor2()
##      time.sleep(1)                                                      
