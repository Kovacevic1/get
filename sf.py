import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BCM)
leds = [9, 10, 22, 27, 17, 4, 3, 2]
aux = [21, 20, 26, 16, 19, 25, 23, 24]
GPIO.setup(leds, GPIO.OUT, initial = 0)
time.sleep(3)
GPIO.setup(aux, GPIO.IN)
try:
    while True:
        for i in range(len(leds)):
            GPIO.output(leds[i], GPIO.input(aux[i]))
finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()