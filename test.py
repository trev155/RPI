import RPi.GPIO as GPIO
import time

# Test module
BUTTON_PIN=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	while True:
		input_state = GPIO.input(BUTTON_PIN)
		if input_state == False:
			print("Button pressed")
			time.sleep(0.2)
			
finally:
	GPIO.cleanup()
