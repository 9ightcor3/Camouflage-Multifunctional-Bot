#!/usr/bin/env python

 
import numpy as np
import os
import time

import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 

IN5=23
IN6=24
IN7=25
IN8=8
RED = 2                                  #Associate pin 23 to TRIG
GREEN = 3 
BLUE = 4                                  #Associate pin 23 to TRIG

LASER=17

IN1=20
IN2=21
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

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO.output(IN1, False)
GPIO.output(IN2, False)
GPIO.output(IN3, False)
GPIO.output(IN4, False)

GPIO.output(RED, False)
GPIO.output(BLUE, False)
GPIO.output(GREEN, False)


GPIO.output(LASER, False)
##



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




import socket
TCP_IP = '192.168.43.78'
TCP_PORT = 8081
BUFFER_SIZE = 20
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()
print ('Connection address:', addr)
ck=1

def FORWORD():
    print('FORWORD')
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)

def STOP():
    print('STOP')
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)

def LEFT():
    print('LEFT')
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)
    
def RIGHT():
    print('RIGHT')
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)



while ck==1:
    data = conn.recv(BUFFER_SIZE)
    data=data.decode('UTF-8','ignore')
    #if len(data) > 0:
        #conn.send('Data Received \r\n')
    print ("received data:", str(data))
    if str(data) == 'A':
        print('DISPENCE THE MEDICLAL KIT')
        FORWORD()
        time.sleep(2)
        STOP()
        time.sleep(2)
        LEFT()
        time.sleep(2)
        STOP()
        time.sleep(2)
        FORWORD()
        time.sleep(2)
        STOP()
        time.sleep(2)
        break
    if str(data) == 'B':
        print('DISPENCE THE MEDICLAL KIT')
        FORWORD()
        time.sleep(2)
        STOP()
        time.sleep(2)
        RIGHT()
        time.sleep(2)
        STOP()
        time.sleep(2)
        FORWORD()
        time.sleep(2)
        STOP()
        time.sleep(2)
        break
        
conn.close()
