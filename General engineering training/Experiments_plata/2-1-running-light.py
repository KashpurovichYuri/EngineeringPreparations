import RPi.GPIO as GPIO
import time as time

leds = [24, 25, 8, 7, 12, 16, 20, 21]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)

for _ in range(3):
    for pin in leds:
        GPIO.output(pin, 1)
        time.sleep(0.2)
        GPIO.output(pin, 0)

GPIO.output(leds, 0)
GPIO.cleanup()
