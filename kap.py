#!/usr/bin/env python
import os
import time
import RPi.GPIO as GPIO
from datetime import datetime

# Grab the current datetime which will be used to generate dynamic folder names
d = datetime.now()
initYear = "%04d" % (d.year)
initMonth = "%02d" % (d.month)
initDate = "%02d" % (d.day)
initHour = "%02d" % (d.hour)
initMins = "%02d" % (d.minute)

# Define the location where you wish to save files. Set to HOME as default.
# If you run a local web server on Apache you could set this to /var/www/ to make them
# accessible via web browser.
folderToSave = "photo_" + str(initYear) + str(initMonth) + str(initDate) + str(initHour) + str(initMins)
os.mkdir(folderToSave)

# Set the initial serial for saved images to 1
fileSerial = 1

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# set up GPIO output channel
GPIO.setup(33, GPIO.OUT)
t = GPIO.PWM(33, 50)  # Tilt pin 33, frequency = 50Hz (20ms)
GPIO.setup(32, GPIO.OUT)
s = GPIO.PWM(32, 50)  # Shif pin 32, frequency = 50Hz (20ms)

t.start(7.5)
s.start(7.5)


# TakeAShoot
def TakeAShoot(fileSerial):
        d = datetime.now()

        # Set FileSerialNumber to 000X using four digits
        fileSerialNumber = "%04d" % (fileSerial)

        # Capture the CURRENT time (not start time as set above) to insert into each capture image filename
        hour = "%02d" % (d.hour)
        mins = "%02d" % (d.minute)

        # Define the size of the image you wish to capture.
        imgWidth = 2592
        imgHeight = 1944
        print " ====================================== Saving file at " + hour + ":" + mins

        # Capture the image using raspistill. Set to capture with added sharpening, auto white balance and average$
        # Change these settings where you see fit and to suit the conditions you are using the camera in
        os.system("raspistill -vf -hf -w " + str(imgWidth) + " -h " + str(imgHeight) + " -o " + str(folderToSave) $

        # Increment the fileSerial
        fileSerial += 1

        # Wait 5 seconds before next capture
        time.sleep(5)

def ServoAngle(angle,pwm):
        DC = 1./18.*(angle)+2
        pwm.ChangeDutyCycle(DC)


try :
        while True:
                for i in range(0,180,60):
                        ServoAngle(i,t)
                        for j in range(0,90,15):
                                ServoAngle(j,s)
                                TakeAShoot(fileSerial)

except KeyboardInterrupt:
        t.stop()
        s.stop()
        GPIO.cleanup()

