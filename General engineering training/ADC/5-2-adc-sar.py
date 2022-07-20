import RPi.GPIO as GPIO
import time


def decimal2binary(val):
    return [int(bit) for bit in bin(val)[2:].zfill(8)]


def num2dac(val):
    sign = decimal2binary(val)
    GPIO.output(dac, sign)
    return sign


def adc():
    l, r = 0, 255  # left and right -> binary search
    while l < r - 1:
        val = (l + r) // 2
        signal = num2dac(val)
        time.sleep(0.07)
        compVal = GPIO.input(comp)
        if not compVal:
            r = val
        else:
            l = val
    return 3.3 * l / 255


dac = [10, 9, 11, 5, 6, 13, 19, 26]  # DAC
comp = 4  # GPIO-pin correspondent to comparator
troyka = 17  # GPIO-pin correspondent to TROYKA-MODULE
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        print(adc())
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
