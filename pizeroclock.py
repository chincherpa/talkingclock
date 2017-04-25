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

while(count < 5):
   now = datetime.datetime.now()
   hour = now.hour
   minute = now.minute
   second = now.second
   currenttime = [ int(hour / 10), hour % 10, int(minute / 10), minute % 10 ]

   Display.Show(currenttime)
   Display.ShowDoublepoint(second % 2)

   time.sleep(1)
   count += 1
   print count

time.sleep(1)
Display.Clear()