from  RPi import GPIO
from time import sleep

DEFAULT_PINS = [ 3, 5, 7, 8, 10 ]
BLINK_DELAY = 0.25

class Defcon:
    level = 0
    outputs = [ False ] * 5

    def __init__(self, pins = DEFAULT_PINS):
        self.pins = pins
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pins, GPIO.OUT)
        self.set_to(0)

    def set_to(self, level):
        self.level = level
        self.outputs = [ False ] * 5
        if level != 0:
            self.outputs[self.level - 1] = True
        self.update()

    def move_to(self, level):
        if level == self.level:
            return
        if level == 0:
            for i in range(3):
                self.outputs[self.level-1] = False
                self.update()
                sleep(BLINK_DELAY)
                self.outputs[self.level-1] = True
                self.update()
                sleep(BLINK_DELAY)
        else:
            for i in range(3):
                self.outputs[level-1] = True
                self.update()
                sleep(BLINK_DELAY)
                self.outputs[level-1] = False
                self.update()
                sleep(BLINK_DELAY)
        self.set_to(level)

    def update(self):
        for i in range(5):
            GPIO.output(self.pins[i], GPIO.HIGH if self.outputs[i] else GPIO.LOW)
