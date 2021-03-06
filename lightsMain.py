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
    upIn = not GPIO.input(up)
    downIn = not GPIO.input(down)
    onoffIn = not GPIO.input(onoff)

    if upIn:                        # Handle button presses
        print('up')
        if state < 4:
            state += 1
    if downIn:
        print('down')
        if state > 1:
            state -= 1
    if onoffIn:
        print('onoff')
        if state > 0:
            oldstate = state
            state = 0
        elif state == 0:
            state = oldstate

    if state == 0:                  # All lights off
        GPIO.output(red, True)
        GPIO.output(blue, True)
        GPIO.output(black, True)
        GPIO.output(gold, True)
    elif state == 1:                # Red on
        GPIO.output(red, False)
        GPIO.output(blue, True)
        GPIO.output(black, True)
        GPIO.output(gold, True)
    elif state == 2:                # Red, Blue on
        GPIO.output(red, False)
        GPIO.output(blue, False)
        GPIO.output(black, True)
        GPIO.output(gold, True)
    elif state == 3:                # Red, Blue, Black on
        GPIO.output(red, False)
        GPIO.output(blue, False)
        GPIO.output(black, False)
        GPIO.output(gold, True)
    elif state == 4:                # All lights on
        GPIO.output(red, False)
        GPIO.output(blue, False)
        GPIO.output(black, False)
        GPIO.output(gold, False)

    print(state)
    
    while not GPIO.input(up) or not GPIO.input(down) or not GPIO.input(onoff):   # Stall in this loop if any buttons are still held down
        pass
    
    time.sleep(0.1)

