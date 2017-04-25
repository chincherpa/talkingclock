import mypi
from tm1637 import TM1637
import time

BRIGHT_TYPICAL = 2

Display = TM1637(23,24,BRIGHT_TYPICAL)
Display.Clear()

count = 10
while count >= 0:
    Display.ShowInt(count)
    time.sleep(1)
    count -= 1

Display.Clear()
time.sleep(1)

myip = mypi.getIP('wlan0')
#print("Wireless IP Address  : " + myip)

numbers = myip.split(".")

# Loop and print each city name.
#loops = 3
#while loops > 0:
for number in numbers:
#    print str(number)
    Display.ShowInt(number)
    time.sleep(1)
#    loops -= 1
#    Display.Clear()
#    time.sleep(1)

#print('done.')
Display.Clear()
