import RPi.GPIO as GPIO
import time as time
#  import random

dac = [10, 9, 11, 5, 6, 13, 19, 26]
number = [0 for _ in range(len(dac))]
number = [1, 1, 1, 1, 1, 1, 1, 1]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

'''for i in range(len(number)):
    number[i] = random.randint(0, 1)'''
GPIO.output(dac, number)

time.sleep(15)

GPIO.output(dac, 0)
GPIO.cleanup()

res = [(0, 0.482), (5, 0.482), (32, 0.483), (64, 0.498), (127, 0.814), (255, 3.248), (256, '?')]