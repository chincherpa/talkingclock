import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)

count = 1

while count < 3:
    input_state = GPIO.input(20)
    if not input_state:
        print "Button pressed #" + str(count)
        count += 1
        time.sleep(1)
        print "-"
