import RPi.GPIO as GPIO
#  import time

leds = [24, 25, 8, 7, 12, 16, 20, 21]
aux = [2, 3, 14, 15, 18, 27, 23, 22]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)

while True:
    for i in range(len(aux)):
        GPIO.output(leds[i], GPIO.input(aux[i]))
