import RPi.GPIO as GPIO
import time

"""
A simple module that takes in a button press as input,
and tells the LED to go on whenever the button is pressed.
"""

BUTTON_PIN=18
LED_PIN=21

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
	while True:
		input_state = GPIO.input(BUTTON_PIN)
		if input_state == False:
			print("Button pressed")
			GPIO.output(LED_PIN, 1)
			time.sleep(0.5)
		else:
			GPIO.output(LED_PIN, 0)
			
finally:
	GPIO.cleanup()
