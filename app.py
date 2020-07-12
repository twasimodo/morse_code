#!/usr/bin/env python3
########################################################################
# Filename    : ButtonLED.py
# Description : Control led with button
# auther      : www.freenove.com
# modification: 2019/12/28
########################################################################
import RPi.GPIO as GPIO
import time

ledPin = 11    # define ledPin
buttonPin = 12    # define buttonPin
shortWait = 0.125 # define short wait for dot and rest
longWait = 0.375 # define long wait for dash
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
def blink(duration):
    GPIO.output(ledPin, GPIO.HIGH)  # make ledPin output HIGH level to turn on led
    time.sleep(duration)                   # Wait for 1 second
    pause(shortWait)

class Letter:
    def __init__(self, letter, morse):
        self.letter = letter
        self.morse = morse
        
    def morse_output(self):
        print(self.letter)
        for char in self.morse:
            beeps[char]()
        space()

def dash():
    print('-', end='')
    blink(longWait)
    
def dot():
    print('.', end='')
    blink(shortWait)
    
def pause(duration):
    GPIO.output(ledPin, GPIO.LOW)   # make ledPin output LOW level to turn off led
    time.sleep(duration)
    
def space():
    print(' ')
    pause(2*shortWait)
    
alphabet = {
    'a': Letter('a','.-'),
    'b': Letter('b','-...'),
    'c': Letter('c','-.-.'),
    'd': Letter('d','-..'),
    'e': Letter('e','.'),
    'f': Letter('f','..-.'),
    'g': Letter('g','--.'),
    'h': Letter('h','....'),
    'i': Letter('i','..'),
    'j': Letter('j','.---'),
    'k': Letter('k','-.-'),
    'l': Letter('l','.-..'),
    'm': Letter('m','--'),
    'n': Letter('n','-.'),
    'o': Letter('o','---'),
    'p': Letter('p','.--.'),
    'q': Letter('q','--.-'),
    'r': Letter('r','.-.'),
    's': Letter('s','...'),
    't': Letter('t','-'),
    'u': Letter('u','..-'),
    'v': Letter('v','...-'),
    'w': Letter('w','.--'),
    'x': Letter('x','-..-'),
    'y': Letter('y','-.--'),
    'z': Letter('z','--..'),
    '1': Letter('1','.----'),
    '2': Letter('2','..---'),
    '3': Letter('3','...--'),
    '4': Letter('4','....-'),
    '5': Letter('5','.....'),
    '6': Letter('6','-....'),
    '7': Letter('7','--...'),
    '8': Letter('8','---..'),
    '9': Letter('9','----.'),
    '0': Letter('0','-----'),
    ' ': Letter(' ','')
}

beeps = {
    ".": dot,
    "-": dash,
    " ": space
}

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

