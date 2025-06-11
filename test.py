#!/bin/env python

# minimal dialog test to PI Model B GPIO ports

import sys
from  RPi import GPIO

PINS = [ 3, 5, 7, 8, 10 ]
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PINS, GPIO.OUT)

def output(v):
    if isinstance(v, int):
        for pin in PINS:
            GPIO.output(pin, GPIO.HIGH if (v & 1) else GPIO.LOW)
            v >>= 1
    elif isinstance(v, tuple) or isinstance(v, list):
        i = len(v)-1
        for pin in PINS:
            GPIO.output(pin, GPIO.HIGH if v[i] else GPIO.LOW)
            i -= 1


if __name__ == 'main':
    output(int(sys.argv[1]))