import RPi.GPIO as GPIO
import time


def initialRight():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setwarnings(False)

    #Right
    GPIO.setup(33, GPIO.OUT)
    GPIO.setup(29, GPIO.OUT)
    GPIO.setup(31, GPIO.OUT)

    right = GPIO.PWM(33,100)
    return right

def aheadRight():
    GPIO.output(29, True)
    GPIO.output(31, False)

def powerRight(motorSide,power):    

    motorSide.start(power)

    for i in range(0,power):
        motorSide.ChangeDutyCycle(power - i)
        time.sleep(0.02)

def stop(motorSide):
    motorSide.stop()

right=initialRight()
aheadRight()

powerRight(right,100)
time.sleep(0.2)
powerRight(right,75)
time.sleep(0.2)
powerRight(right,100)
time.sleep(0.2)

stop(right)
