import RPi.GPIO as GPIO
import time
import patterns

# Define pin number constants
LED_1 = 25
LED_2 = 24
LED_3 = 23
LED_4 = 21
LED_5 = 20
LED_6 = 16
LED_MID_R = 13
LED_MID_G = 19
LED_MID_B = 26
BUTTON_LEFT=22
BUTTON_RIGHT=27

ALL_PATTERNS = ["A", "B", "C", "D"]
DEFAULT_PATTERN = "A"

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_1, GPIO.OUT)
GPIO.setup(LED_2, GPIO.OUT)
GPIO.setup(LED_3, GPIO.OUT)
GPIO.setup(LED_4, GPIO.OUT)
GPIO.setup(LED_5, GPIO.OUT)
GPIO.setup(LED_6, GPIO.OUT)
GPIO.setup(LED_MID_R, GPIO.OUT)
GPIO.setup(LED_MID_G, GPIO.OUT)
GPIO.setup(LED_MID_B, GPIO.OUT)
GPIO.setup(BUTTON_LEFT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

"""
Run the following configuration given by config. 
A configuration is a tuple that consists of the following:
(L1, L2, L3, L4, L5, L6, (M1, M2, M3), TO)
where
L1 is the left most LED,
L6 is the right most LED,
(M1, M2, M3) is a tuple representing the middle RGB LED,
TO is the timeout value - amount of milliseconds to wait 
after executing this configuration.
"""
def configuration(config):
	led_1 = config[0]
	led_2 = config[1]
	led_3 = config[2]
	led_4 = config[3]
	led_5 = config[4]
	led_6 = config[5]
	led_mid = config[6]
	led_mid_r = led_mid[0]
	led_mid_g = led_mid[1]
	led_mid_b = led_mid[2]
	timeout = config[7]

	GPIO.output(LED_1, led_1)
	GPIO.output(LED_2, led_2)
	GPIO.output(LED_3, led_3)
	GPIO.output(LED_4, led_4)
	GPIO.output(LED_5, led_5)
	GPIO.output(LED_6, led_6)
	GPIO.output(LED_MID_R, led_mid_r)
	GPIO.output(LED_MID_G, led_mid_g)
	GPIO.output(LED_MID_B, led_mid_b)
	
	time.sleep(timeout)

def run_pattern(pattern, step):
	configuration(pattern[step])

def next_pattern(current_pattern):
	current_pattern_index = ALL_PATTERNS.index(current_pattern)
	if current_pattern_index == len(ALL_PATTERNS) - 1:
		return ALL_PATTERNS[0]
	return ALL_PATTERNS[current_pattern_index + 1]

if __name__ == "__main__":
	leftIsPressed = False
	rightIsPressed = False
	current_pattern = DEFAULT_PATTERN
	current_step = 0

	try:
		while True:
			left_button = not GPIO.input(BUTTON_LEFT)
			right_button = not GPIO.input(BUTTON_RIGHT)
			if left_button:
				leftIsPressed = True
			elif leftIsPressed:
				current_pattern = DEFAULT_PATTERN
				current_step = 0
				leftIsPressed = False
				print("Left button pressed. Reset")

			if right_button:
				rightIsPressed = True
			elif rightIsPressed:
				current_pattern = next_pattern(current_pattern)
				current_step = 0
				rightIsPressed = False
				print("Right button pressed. Advance to next pattern", current_pattern)

			# Run the next step in the pattern
			run_pattern(patterns.return_pattern(current_pattern), current_step)
			current_step = current_step + 1
			if (len(patterns.return_pattern(current_pattern)) == current_step):
				print("Pattern complete, resetting")
				current_step = 0

	finally:
		GPIO.cleanup()
