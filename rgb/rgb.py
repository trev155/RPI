import RPi.GPIO as GPIO
import time

BUTTON_LEFT=18
BUTTON_RIGHT=23
LED_LEFT=16
LED_MID=20
LED_RIGHT=21

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_LEFT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_LEFT, GPIO.OUT)
GPIO.setup(LED_MID, GPIO.OUT)
GPIO.setup(LED_RIGHT, GPIO.OUT)

print("Module is ready - press a button!")

try:
	while True:
		left_button = GPIO.input(BUTTON_LEFT)
		right_button = GPIO.input(BUTTON_RIGHT)
		if not left_button or not right_button:
			print("Button pressed")
			if not left_button and not right_button:
				GPIO.output(LED_LEFT, 0)
				GPIO.output(LED_MID, 1)
				GPIO.output(LED_RIGHT, 1)
		else:
			GPIO.output(LED_LEFT, 0)
			GPIO.output(LED_MID, 0)
			GPIO.output(LED_RIGHT, 0)
		time.sleep(0.2)
finally:
	GPIO.cleanup()

