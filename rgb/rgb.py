import RPi.GPIO as GPIO
import time
import itertools

BUTTON_LEFT=18
BUTTON_RIGHT=23
LED_LEFT=16
LED_MID=20
LED_RIGHT=21

LED_MAPS = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)]
LED_MAP_INDEX = 0
LED_MAP = LED_MAPS[LED_MAP_INDEX]

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_LEFT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_LEFT, GPIO.OUT)
GPIO.setup(LED_MID, GPIO.OUT)
GPIO.setup(LED_RIGHT, GPIO.OUT)

print("Module is ready - press a button!")

try:
	while True:
		right_button_pressed = not GPIO.input(BUTTON_RIGHT)
		if right_button_pressed:
			print("Button pressed")
			# Change LED map config
			LED_MAP_INDEX = LED_MAP_INDEX + 1
			if LED_MAP_INDEX == len(LED_MAPS):
				LED_MAP_INDEX = 0
			LED_MAP = LED_MAPS[LED_MAP_INDEX]
			print(LED_MAP)
		GPIO.output(LED_LEFT, LED_MAP[0])
		GPIO.output(LED_MID, LED_MAP[1])
		GPIO.output(LED_RIGHT, LED_MAP[2])
		time.sleep(0.1)
finally:
	GPIO.cleanup()

