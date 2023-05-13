#!/usr/bin/env python

import RPi.GPIO as GPIO
import time


class motor_28byj48:
    def __init__(self, pins):
        self.pins = pins
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pins, GPIO.OUT)

    def __del__(self):
        GPIO.cleanup()

    def setStep(self, w1, w2, w3, w4):
        GPIO.output(self.pins[0], w1)
        GPIO.output(self.pins[1], w2)
        GPIO.output(self.pins[2], w3)
        GPIO.output(self.pins[3], w4)

    def forward(self, delay, steps):
        for i in range(0, steps):
            self.setStep(1, 0, 0, 0)
            time.sleep(delay)
            self.setStep(0, 1, 0, 0)
            time.sleep(delay)
            self.setStep(0, 0, 1, 0)
            time.sleep(delay)
            self.setStep(0, 0, 0, 1)
            time.sleep(delay)

    def backward(self, delay, steps):
        for i in range(0, steps):
            self.setStep(0, 0, 0, 1)
            time.sleep(delay)
            self.setStep(0, 0, 1, 0)
            time.sleep(delay)
            self.setStep(0, 1, 0, 0)
            time.sleep(delay)
            self.setStep(1, 0, 0, 0)
            time.sleep(delay)

    def stop(self):
        self.setStep(0, 0, 0, 0)
