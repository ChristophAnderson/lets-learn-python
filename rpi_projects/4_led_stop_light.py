import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
interval = 0.05
while 1:
        print "Let's do it!"
        GPIO.output(6, GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(26, GPIO.LOW)
        time.sleep(interval)
        GPIO.output(19, GPIO.HIGH)
        GPIO.output(6, GPIO.LOW)
        time.sleep(interval)
        GPIO.output(26, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
        time.sleep(interval)
        GPIO.output(19, GPIO.LOW)
        time.sleep(interval)
        GPIO.output(26, GPIO.LOW)