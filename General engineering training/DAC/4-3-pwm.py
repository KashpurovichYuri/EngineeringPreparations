import RPi.GPIO as GPIO
import time


def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
pwm = GPIO.PWM(22, 1000)
pwm.start(0)

try:
    dc = input()
    while dc != 'q':
        pwm.start(int(dc))
        print('There will be voltage about:', str(3.3 * int(dc) / 100))
        dc = input()
finally:
    pwm.stop()
    GPIO.output(22, 0)
    GPIO.cleanup()
