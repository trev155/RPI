import RPi.GPIO as GPIO
import time

"""
A module that has 2 input buttons. 
"""

BUTTON_LEFT=23
BUTTON_RIGHT=18
LED_LEFT=21
LED_MID=16
LED_RIGHT=12

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_LEFT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_LEFT, GPIO.OUT)
GPIO.setup(LED_MID, GPIO.OUT)
GPIO.setup(LED_RIGHT, GPIO.OUT)

try:
	while True:
		left_button = GPIO.input(BUTTON_LEFT)
		right_button = GPIO.input(BUTTON_RIGHT)
		if left_button == False or right_button == False:
			print("Button pressed")
			GPIO.output(LED_LEFT, 1)
			time.sleep(0.5)
		else:
			GPIO.output(LED_LEFT, 0)
			
finally:
	GPIO.cleanup()
