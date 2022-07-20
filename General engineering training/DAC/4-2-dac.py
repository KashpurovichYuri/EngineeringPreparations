import RPi.GPIO as GPIO
import time


def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [10, 9, 11, 5, 6, 13, 19, 26][::-1]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    tau = float(input())
    while True:
        for i in [1, 3, 7, 15, 31, 63, 127, 255]:
            _bin = decimal2binary(i)
            for j in range(len(_bin)):
                time.sleep(tau)
                GPIO.output(dac[j], _bin[j])
        time.sleep(tau)
        for i in [1, 3, 7, 15, 31, 63, 127, 255][::-1]:
            _bin = decimal2binary(i)
            for j in range(len(_bin)):
                time.sleep(8*tau)
                GPIO.output(dac[j], 0)
    
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
