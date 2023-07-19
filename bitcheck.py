import random
import RPi.GPIO as pin
import time

pin.setmode(pin.BCM)

S1 = 18
S2 = 23
S3 = 24
S4 = 25
S5 = 12
S6 = 16
S7 = 20
S8 = 21
switches = [S1, S2, S3, S4, S5, S6, S7, S8]
pin.setup(switches, pin.OUT)

feedback = 26
pin.setup(feedback, pin.OUT)



def bitcheck(s, f):
    random.shuffle(s)

    fail = False
    for io in s:
        toggle(io, 1)
        time.sleep(1)

        pin.setup(io, pin.IN)
        if pin.input(io)==0: # I believe this is inverted to what one may think it'd be
            fail = True
        else:
            pass
    
    if fail == True:
        toggle(f, 1)
    else:
        toggle(f, 0)
    
    time.sleep(10)

    for io in s:
        toggle(io, 0)
    toggle(f, 0)

    pin.cleanup()


def toggle(p, o):
    # p = Pin Number
    # o = Pin Value : either 1 or 0 --- This is an alternative to GPIO.HIGH or GPIO.LOW, or True or False
    pin.output(p, o)