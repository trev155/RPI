import time
import sys
import RPi.GPIO as GPIO

# Constants
LED_PIN = 21

# Command line parsing
if len(sys.argv) < 3:
	print("Usage: " + sys.argv[0] + " " + "<blink_count> <interval_time>")
	sys.exit()
blink_count = int(sys.argv[1])
interval_time = float(sys.argv[2])

# Must have these GPIO setup functions
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Main loop - turn the LED on, then off. Wait some amount of time
# for transitions. At the end, cleanup the GPIO pin configs.
num_blinks = 0
try:
    while (num_blinks < blink_count):
        print("LED ON")
        GPIO.output(LED_PIN, 1)
        time.sleep(interval_time)
        print("LED OFF")
        GPIO.output(LED_PIN, 0)
        time.sleep(interval_time)
        num_blinks = num_blinks + 1
finally:
    GPIO.cleanup()


