#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
 
#set GPIO Pins
GPIO_TRIGGER = 11
GPIO_ECHO = 13
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

kalman=[-1,-1,-1]
estimacion=-1

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            if (dist > 1000.0):
                print (".")
            else:
                if (kalman[0] ==-1):
                    for x in range (0,3):
                        kalman[x] = dist
                else:
                    kalman[0] = (0.4*kalman[0] + 0.6*dist)
                    kalman[1] = (0.3*kalman[1] + 0.7*dist)
                    kalman[2] = (0.2*kalman[2] + 0.8*dist)
                    estimacion = (kalman[0]+kalman[1]+kalman[2])/3.0
                print ("Measured Distance = %.1f cm (kalman: %.1f, %.1f, %.1f)(estimacion: %.1f)" % (dist, kalman[0],kalman[1],kalman[2],estimacion))
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
