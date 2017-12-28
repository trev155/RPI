import RPi.GPIO as GPIO
import time

LED_1 = 24
LED_2 = 23
LED_3 = 18
LED_4 = 21
LED_5 = 20
LED_6 = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_1, GPIO.OUT)
GPIO.setup(LED_2, GPIO.OUT)
GPIO.setup(LED_3, GPIO.OUT)
GPIO.setup(LED_4, GPIO.OUT)
GPIO.setup(LED_5, GPIO.OUT)
GPIO.setup(LED_6, GPIO.OUT)

try:
	GPIO.output(LED_1, 1)
	GPIO.output(LED_2, 1)
	GPIO.output(LED_3, 1)
	GPIO.output(LED_4, 1)
	GPIO.output(LED_5, 1)
	GPIO.output(LED_6, 1)	
	time.sleep(2)
	GPIO.output(LED_1, 0)
	GPIO.output(LED_2, 0)
	GPIO.output(LED_3, 0)
	GPIO.output(LED_4, 0)
	GPIO.output(LED_5, 0)
	GPIO.output(LED_6, 0)
finally:
	GPIO.cleanup()
