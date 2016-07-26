
import RPi.GPIO as GPIO
import time
# servo controller function

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# set up GPIO output channel
GPIO.setup(33, GPIO.OUT)
t = GPIO.PWM(33, 50)  # Tilt pin 33, frequency = 50Hz (20ms)

GPIO.setup(32, GPIO.OUT)
s = GPIO.PWM(32, 50)  # Shif pin 32, frequency = 50Hz (20ms)



t.start(7.5)
s.start(7.5)

try :
	while True:
		t.ChangeDutyCycle(7.5)
		time.sleep(10)

	        s.ChangeDutyCycle(7.5)
        	time.sleep(10)
                s.ChangeDutyCycle(5)
                time.sleep(10)
                s.ChangeDutyCycle(2.5)
       	        time.sleep(10)

		
                t.ChangeDutyCycle(12.5)
                time.sleep(10)

                s.ChangeDutyCycle(7.5)
                time.sleep(10)
                s.ChangeDutyCycle(5)
                time.sleep(10)
                s.ChangeDutyCycle(2.5)
                time.sleep(10)



                t.ChangeDutyCycle(2.5)
                time.sleep(10)

                s.ChangeDutyCycle(7.5)
		time.sleep(10)
                s.ChangeDutyCycle(5)
                time.sleep(10)
                s.ChangeDutyCycle(2.5)
                time.sleep(10)




except KeyboardInterrupt:
	t.stop()
	s.stop()
	GPIO.cleanup()
