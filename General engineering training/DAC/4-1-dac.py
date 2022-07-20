import RPi.GPIO as GPIO


def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


dac = [10, 9, 11, 5, 6, 13, 19, 26]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    print('Enter number from 0 to 255')
    num = input()
    while num != 'q':
        if not num.isnumeric():
            print('Entered not integer value')
        elif float(num) < 0:
            print('Entered negative value')
        elif float(num) > 255:
            print('Entered too large value')
        else:
            _bin = decimal2binary(int(num))

            '''V = 0.0
            for i in range(1, 9):
                V += V * _bin[i - 1] / 2 ** (9 - i)'''

            print('There will be voltage about:', str(3.3 * int(num) / 256))
            #  print(''.join(map(str, _bin)))
            for i in range(len(_bin[::-1])):
                GPIO.output(dac[i], _bin[::-1][i])
                
        print('Enter number from 0 to 255')
        num = input()
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
