# Sense Hat - Binary Clock
# (c) Barry Bridgens 2022

from sense_hat import SenseHat
from datetime import datetime
from time import sleep

sense = SenseHat()


def clear_row(row):
    for x in range(8):
        sense.set_pixel(x, row, 0, 0, 0)

def set_row(row, number, colour):
    for x in range(8):
        if ((number & 2**x) == 2**x):
            sense.set_pixel((7 - x), row, colour)
        else:
            sense.set_pixel((7 -x), row, (0, 0, 0))



red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

while(1):

    now = datetime.today()

    #for row in range(8):
    #    clear_row(row)

    set_row(0, (now.year - 2000), red)
    set_row(1, now.month, red)
    set_row(2, now.day, red)
    set_row(3, now.hour, blue)
    set_row(4, now.minute, blue)
    set_row(5, now.second, blue)
    #set_row(6, int(now.microsecond / 10000), green)

    sleep(1)
