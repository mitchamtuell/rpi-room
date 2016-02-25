import RPi.GPIO as GPIO
import time

red = 2
blue = 3
black = 14
gold = 4

GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(black, GPIO.OUT)
GPIO.setup(gold, GPIO.OUT)

while True:
    GPIO.output(red, False)
    GPIO.output(blue, False)
    GPIO.output(black, False)
    GPIO.output(gold, False)

    time.sleep(1)

    GPIO.output(red, True)
    GPIO.output(blue, True)
    GPIO.output(black, True)
    GPIO.output(gold, True)

    time.sleep(1)
