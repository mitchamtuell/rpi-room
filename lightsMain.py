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

state = 4
oldstate = 0

while True:                         # Main loop
    upIn = GPIO.input(up)
    downIn = GPIO.input(down)
    onoffIn = GPIO.input(onoff)

    if state == 0:                  # All lights off
        GPIO.output(red, False)
        GPIO.output(blue, False)
        GPIO.output(black, False)
        GPIO.output(gold, False)
    elif state == 1:                # Red on
        GPIO.output(red, True)
        GPIO.output(blue, False)
        GPIO.output(black, False)
        GPIO.output(gold, False)
    elif state == 2:                # Red, Blue on
        GPIO.output(red, True)
        GPIO.output(blue, True)
        GPIO.output(black, False)
        GPIO.output(gold, False)
    elif state == 3:                # Red, Blue, Black on
        GPIO.output(red, True)
        GPIO.output(blue, True)
        GPIO.output(black, True)
        GPIO.output(gold, False)
    elif state == 4:                # All lights on
        GPIO.output(red, True)
        GPIO.output(blue, True)
        GPIO.output(black, True)
        GPIO.output(gold, True)

    if upIn:                        # Handle button presses
        if state < 4:
            state += 1
    if downIn:
        if state > 1:
            state -= 1
    if onoffIn:
        if state > 0:
            oldstate = state
            state = 0
        elif state == 0:
            state = oldstate

    print(state)
    time.sleep(0.1)

