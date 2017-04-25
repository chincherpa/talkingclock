import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)

ianzahl = 9
count = 1

print "waiting..."
while count < ianzahl:
	input_state = GPIO.input(20)
	if not input_state:
		print "Button pressed #" + str(count)
		os.system('aplay sounds/0' + str(count) + '.wav')
		time.sleep(2)		#zusaetzlichen Druck vermeiden
		count += 1
		if count <= ianzahl:
			print "waiting..."
