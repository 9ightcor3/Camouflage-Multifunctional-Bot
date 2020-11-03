# Import OpenCV2 for image processing
import cv2
import os
import time
##from twilio.rest import Client


import RPi.GPIO as GPIO
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

IR=19
LASER=17

IN5=23
IN6=24
IN7=25
IN8=8

RED = 2                                  #Associate pin 23 to TRIG
GREEN = 3 
BLUE = 4                                  #Associate pin 23 to TRIG

GPIO.setup(RED,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(GREEN,GPIO.OUT)   
GPIO.setup(BLUE,GPIO.OUT)


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(IR, GPIO.IN)
GPIO.setup(LASER, GPIO.OUT)

GPIO.setup(IN5, GPIO.OUT)
GPIO.setup(IN6, GPIO.OUT)
GPIO.setup(IN7, GPIO.OUT)
GPIO.setup(IN8, GPIO.OUT)


GPIO.output(IN5, False)
GPIO.output(IN6, False)
GPIO.output(IN7, False)
GPIO.output(IN8, False)

GPIO.output(RED, False)
GPIO.output(BLUE, False)
GPIO.output(GREEN, False)

##GPIO.output(LASER, False)


def forward():
    GPIO.output(IN7, True)
    GPIO.output(IN8, False)
##    if(GPIO.input(IR) == False):
##        mon=1
##        print('PERSON DETECTED')
        
def reverse():
    GPIO.output(IN7, False)
    GPIO.output(IN8, True)
##    if(GPIO.input(IR) == False):
##        mon=1
##        print('PERSON DETECTED')

##    time.sleep(5)
def stop():
    GPIO.output(IN7, False)
    GPIO.output(IN8, False)

def IR():
    if(GPIO.input(26) == False):
        stop()
        mon=1
        print('PERSON DETECTED')


##GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
# Import numpy for matrices calculations
import numpy as np
import time
import datetime
# Create Local Binary Patterns Histograms for face recognization
#recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the trained mode
recognizer.read('trainer/trainer.yml')
##recognizer.read('/home/pi/Desktop/face_recog_folder/Raspberry-Face-Recognition-master/trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)

flag = []
count1=0
count2=0
count3=0
sample =0
lecture=0
mon=0
count=0


##account_sid = "AC4c80a8d4e94004afc637499ca50ddc59"
##auth_token = "d7008f6cd8700dd6fac792bc35f7bfa7"
##
##client = Client(account_sid, auth_token)

while True:
    forward()
    time.sleep(2)

    stop()
    time.sleep(1)

    reverse()
    time.sleep(2)
    stop()
    time.sleep(1)

    if(GPIO.input(19) == False):
     
        mon=1
   
        print('PERSON DETECTED')
     
    
    while mon == 1:
        now = datetime.datetime.now()

        # Read the video frame
        ret, im =cam.read()

        # Convert the captured frame into grayscale
        gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

        # Get all face from the video frame
        faces = faceCascade.detectMultiScale(gray, 1.2,5)

        # For each face in faces
        for(x,y,w,h) in faces:

            # Create rectangle around the face
            cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

            # Recognize the face belongs to which ID
            Id,i = recognizer.predict(gray[y:y+h,x:x+w])
            #id = int(os.path.split(imagePath)[-1].split(".")[1])
            
            print(i)
            # Check the ID if exist
            if i < 60:
                sample= sample+1
                if Id == 2 :
                    #flag[1]=1
                    count1=1
                    Id = "SAMEER"
                    print("SAMEER")
                    lecture=1
                    sample=0
                    forward()
                    time.sleep(1)
                    stop()
                    time.sleep(2)
                    reverse()
                    time.sleep(1)
                    stop()
                    time.sleep(2)
                    #time.sleep(2)
                    break
                   

               
            else:
                count=count+1

                if count > 20:
                    count=0
                    print(Id)
                    mon=0
                    Id = "unknown"
                    stop()
                    print('LASER GUN ON')
                    GPIO.output(LASER, GPIO.HIGH)
                    cv2.imwrite('frame.png',im)
##                    client.api.account.messages.create(
##    to="+91-9902599273",
##    from_="+1 716-543-3315" ,  #+1 210-762-4855"
##    body=" Detected" )
##                    atttachem.sendMail( ["ashokkoppad21@gmail.com"],
##        "Unknown person Detected",
##        "Unknown person Detected",
##        ["frame.png","test.txt"] )
            
            # Put text describe who is in the picture
            cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
            cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)

            # Display the video frame with the bounded rectangle
            cv2.imshow('im',im)


        # If 'q' is pressed, close program
        if cv2.waitKey(20) & 0xFF == ord('q'): #if cv2.waitKey(10) & 0xFF == ord('q'):
            break
           
cam.release()

# Close all windows
cv2.destroyAllWindows()
