import RPi.GPIO as GPIO
import time

BUTTON_LEFT=18
BUTTON_RIGHT=23
LED_LEFT=16
LED_MID=20
LED_RIGHT=21

LED_MAP = [False, False, False]

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_LEFT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_LEFT, GPIO.OUT)
GPIO.setup(LED_MID, GPIO.OUT)
GPIO.setup(LED_RIGHT, GPIO.OUT)

print("Module is ready - press a button!")

try:
	while True:
		# left_button = GPIO.input(BUTTON_LEFT)
		right_button_pressed = not GPIO.input(BUTTON_RIGHT)
		if right_button_pressed:
			print("Button pressed")
			# Change LED map config
		else:
			GPIO.output(LED_LEFT, LED_MAP[0])
			GPIO.output(LED_MID, LED_MAP[1])
			GPIO.output(LED_RIGHT, LED_MAP[2])
		time.sleep(0.2)
finally:
	GPIO.cleanup()

