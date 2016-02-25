import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

red = 2
blue = 3
black = 14
gold = 4

down = 17
up = 27
onoff = 22

GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(black, GPIO.OUT)
GPIO.setup(gold, GPIO.OUT)

GPIO.setup(down, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(onoff, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    upIn = GPIO.input(up)
    downIn = GPIO.input(down)
    onoffIn = GPIO.input(onoff)

    if upIn:
        GPIO.output(red, True)
    else:
        GPIO.output(red, False)

    if downIn:
        GPIO.output(blue, True)
    else:
        GPIO.output(blue, False)

    if onoffIn:
        GPIO.output(black, True)
    else:
        GPIO.output(black, False)

    time.sleep(0.1)

