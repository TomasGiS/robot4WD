import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

#Right
GPIO.setup(33, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)

#Left
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

GPIO.output(29, False)
GPIO.output(31, False)

GPIO.output(33,False)

GPIO.output(16,False)
GPIO.output(18,False)

GPIO.output(12,False)
