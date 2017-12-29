import RPi.GPIO as GPIO
import time


def initialLeft():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setwarnings(False)

    #Left
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)

    left = GPIO.PWM(12,100)
    return left

def aheadLeft():
    GPIO.output(18, True)
    GPIO.output(16, False)

def powerLeft(motorSide,power):    

    motorSide.start(power)

    for i in range(0,power):
        motorSide.ChangeDutyCycle(power - i)
        time.sleep(0.02)

def stop(motorSide):
    motorSide.stop()

left=initialLeft()
aheadLeft()

powerLeft(left,100)
time.sleep(0.2)
powerLeft(left,75)
time.sleep(0.2)
powerLeft(left,100)
time.sleep(0.2)

stop(left)

GPIO.cleanup()

