import RPi.GPIO as GPIO
import time
import random
import matplotlib.pyplot as plt
GPIO.setmode(GPIO.BCM)
dac = [6, 12, 5, 0, 1, 7, 11, 8]
number = [0, 0, 0, 0, 0, 1, 1, 0]
GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, number)
time.sleep(1)
GPIO.output(dac, 0)
GPIO.cleanup()
a = [0, 5, 32, 64, 127, 255]
b = [0.04, 0.11, 0.45, 0.86, 1.66, 3.23]
plt.plot(a, b)
plt.show()