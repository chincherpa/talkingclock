#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tm1637 import TM1637
import time
import datetime
import RPi.GPIO as IO 

BRIGHT_TYPICAL = 2

Display = TM1637(23,24,BRIGHT_TYPICAL)
Display.Clear()

count = 0

print "IP of RasPi is"
print IP

# Separate on comma.
numbers = IP.split(".")

# Loop and print each city name.
loops = 3
while loops > 0:
    for number in numbers:
        Display.ShowInt(number)
        time.sleep(2)
    loops -= 1
    Display.Clear()
    time.sleep(2)

print('done.')
Display.Clear()
