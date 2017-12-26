import RPi.GPIO as GPIO
import time

# Test module
BUTTON_PIN=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

isPressed = False

try:
	while True:
		input_state = not GPIO.input(BUTTON_PIN)
		if input_state:
			isPressed = True
		elif isPressed:
			print("Button pressed")
			isPressed = False
		time.sleep(0.2)
			
finally:
	GPIO.cleanup()
