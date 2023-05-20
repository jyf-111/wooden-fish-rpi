import RPi.GPIO as GPIO


class Diode:
    def __init__(self, IN):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(IN, GPIO.OUT)
        self.IN = IN

    def __del__(self):
        GPIO.cleanup(self.IN)

    def turn_on(self):
        GPIO.output(self.IN, GPIO.HIGH)

    def turn_off(self):
        GPIO.output(self.IN, GPIO.LOW)
