import RPi.GPIO as GPIO
import time


class rfp602:
    prev_input = 0

    def __init__(self, press_pin, delay):
        self.press_pin = press_pin
        self.delay = delay

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(press_pin, GPIO.IN)

    def __del__(self):
        GPIO.cleanup(self.press_pin)

    def active(self):
        while True:
            input = GPIO.input(self.press_pin)
            print("{}".format(input))
            if (not self.prev_input) and input:
                print("Under Pressure")
            self.prev_input = input
            time.sleep(self.delay)
