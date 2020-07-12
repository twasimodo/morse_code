import RPi.GPIO as GPIO
import time

class Light:
    def __init__(self, pin):
        self.pin = pin
        self.shortWait = 0.125 # define short wait for dot and rest
        self.longWait = 0.375 # define long wait for dash
        
    def blink(self, duration):
        GPIO.output(self.pin, GPIO.HIGH)  # make ledPin output HIGH level to turn on led
        time.sleep(duration)                   # Wait for 1 second
        self.pause(self.shortWait)

    def dash(self):
        print('-', end='')
        self.blink(self.longWait)
        
    def dot(self):
        print('.', end='')
        self.blink(self.shortWait)

    def space(self):
        print(' ')
        self.pause(2*self.shortWait)
        
    def pause(self, duration):
        GPIO.output(self.pin, GPIO.LOW)   # make ledPin output LOW level to turn off led
        time.sleep(duration)