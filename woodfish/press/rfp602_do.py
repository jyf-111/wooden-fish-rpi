import RPi.GPIO as GPIO


class Rfp602:
    prev_input = 0

    def __init__(self, press_pin, delay):
        self.press_pin = press_pin
        self.delay = delay

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(press_pin, GPIO.IN)

    def __del__(self):
        GPIO.cleanup(self.press_pin)

    def get_input(self):
        return GPIO.input(self.press_pin)
