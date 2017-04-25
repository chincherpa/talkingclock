#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tm1637
from time import sleep
import datetime
import RPi.GPIO as IO 

IO.setwarnings(False)
IO.setmode(IO.BCM)

HexDigits = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71] 

ADDR_AUTO = 0x40
ADDR_FIXED = 0x44
STARTADDR = 0xC0
BRIGHT_DARKEST = 0 
BRIGHT_TYPICAL = 2
BRIGHT_HIGHEST = 7
OUTPUT = IO.OUT
INPUT = IO.IN
LOW = IO.LOW
HIGH = IO.HIGH

# Initialize the display (GND, VCC=3.3V, Example Pins are DIO-20 and CLK21)
Display = tm1637.TM1637(23,24,BRIGHT_TYPICAL)

# Basic Display Update:
digits = [1, 2, 3, 4]
Display.Show(digits)
print "1234  - Working? (Press Key)"
scrap = raw_input()

# Update Individual Digits:
print "Updating one digit at a time:"
Display.Clear()
Display.Show1(1, 3)
print "  3"
sleep(1)
Display.Show1(2, 2)
print "  3 2"
sleep(1)
Display.Show1(3, 1)
print "  3 2 1"
sleep(1)
Display.Show1(0, 4)
print "4 3 2 1"
print "4321  - (Press Key)"
scrap = raw_input()

# The ":"
#print "Add double point\n"
#sleep(2)
#Display.ShowDoublepoint(True)
#sleep(2)

# Vary the brightness:
#print "Brightness Off"
#Display.SetBrightness(0)
#sleep(0.5)
#print "Full Brightness"
#Display.SetBrightness(1)
#sleep(0.5)
#print "30% Brightness"
#Display.SetBrightness(0.3)
#sleep(0.3)

print('done.')
Display.Clear()


