import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt


def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def num2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal


def getnum(arr):
    num = 0
    for i in range(len(arr)):
        num += arr[i] * (2 ** (7 - i))
    return num


def adc():
    arr = [0] * 8
    num = 0
    for i in range(8):
        arr[i] = 1
        num = getnum(arr)
        if i == 8:
            return None
        num2dac(num)
        time.sleep(0.01)
        comp_value = GPIO.input(comp)

        if comp_value == 0:
            arr[i] = 0
    return num


measures = []
leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)

starting_time = time.time()

try:
    while __name__ == '__main__':
        GPIO.output(troyka, 1)
        current = adc()
        time.sleep(1)
        GPIO.output(leds, dec2bin(current))
        num = current / 256 * 3.3
        print(num)
        measures.append(num)
        if num > 3:
            break
    
    GPIO.output(troyka, 0)
    while __name__ == '__main__':
        current = adc()
        time.sleep(0.01)
        GPIO.output(leds, dec2bin(current))
        num = current / 256 * 3.3
        measures.append(num)
        if num < 0.5:
            break
    
    stop_time = time.time()
    print('Total time: ', stop_time - starting_time)
    print('Frequency: ', 1)
    print('Steps: ', 8)
    plt.plot(measures)
    plt.show()

    data = list(map(str, measures))
    with open('./meausres.txt', 'w') as file:
        file.write('\n'.join(measures))

finally:
    GPIO.output(leds, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
