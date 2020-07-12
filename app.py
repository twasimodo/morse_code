#!/usr/bin/env python3
########################################################################
# Filename    : ButtonLED.py
# Description : Control led with button
# auther      : www.freenove.com
# modification: 2019/12/28
########################################################################
import RPi.GPIO as GPIO
import time
from pkg import *

ledPin = 11    # define ledPin
buttonPin = 12    # define buttonPin
sentence = ""

def morse_code():
    print("inside the morse_code function")
    print(sentence)
    for letter in sentence:
        alphabet[letter.lower()].morse_output()

def setup():
    GPIO.setmode(GPIO.BOARD)      # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT)   # set ledPin to OUTPUT mode
    GPIO.output(ledPin, GPIO.LOW)  # make ledPin output LOW level 
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set buttonPin to PULL UP INPUT mode
    global sentence
    sentence = input("Enter sentence:")

def loop():
    while True:
        if GPIO.input(buttonPin)==GPIO.LOW: # if button is pressed
            morse_code()
        else : # if button is relessed
            GPIO.output(ledPin,GPIO.LOW) # turn off led 
            GPIO.output(ledPin,GPIO.LOW) # turn off led 

def destroy():
    GPIO.output(ledPin, GPIO.LOW)     # turn off led 
    GPIO.cleanup()                    # Release GPIO resource

if __name__ == '__main__':     # Program entrance
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()

