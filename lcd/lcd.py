#!/usr/bin/python
#
# HD44780 LCD Test Script for
# Raspberry Pi
#
# Author : Matt Hawkins
# Site   : http://www.raspberrypi-spy.co.uk
# 
# Date   : 03/08/2012
#

# The wiring for the LCD is as follows:
# 1 : GND
# 2 : 5V
# 3 : Contrast (0-5V)*
# 4 : RS (Register Select)
# 5 : R/W (Read Write)       - GROUND THIS PIN
# 6 : Enable or Strobe
# 7 : Data Bit 0             - NOT USED
# 8 : Data Bit 1             - NOT USED
# 9 : Data Bit 2             - NOT USED
# 10: Data Bit 3             - NOT USED
# 11: Data Bit 4
# 12: Data Bit 5
# 13: Data Bit 6
# 14: Data Bit 7
# 15: LCD Backlight +5V**
# 16: LCD Backlight GND

import RPi.GPIO as GPIO
import time
import socket
from enum import Enum

# Define GPIO to LCD mapping
LCD_RS = 24
LCD_E  = 25
LCD_D4 = 12 
LCD_D5 = 16
LCD_D6 = 20
LCD_D7 = 21

# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line 

# Timing constants
E_PULSE = 0.00005
E_DELAY = 0.00005

# Input buttons
BUTTON_LEFT = 5
BUTTON_RIGHT = 26


"""
Initialize GPIO and LCD
"""
def lcd_init():
    GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
    GPIO.setup(LCD_E, GPIO.OUT)  # E
    GPIO.setup(LCD_RS, GPIO.OUT) # RS
    GPIO.setup(LCD_D4, GPIO.OUT) # DB4
    GPIO.setup(LCD_D5, GPIO.OUT) # DB5
    GPIO.setup(LCD_D6, GPIO.OUT) # DB6
    GPIO.setup(LCD_D7, GPIO.OUT) # DB7

    GPIO.setup(BUTTON_LEFT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Initialise display
    lcd_byte(0x33, LCD_CMD)
    lcd_byte(0x32, LCD_CMD)
    lcd_byte(0x28, LCD_CMD)
    lcd_byte(0x0C, LCD_CMD)  
    lcd_byte(0x06, LCD_CMD)
    lcd_byte(0x01, LCD_CMD)  

def lcd_byte(bits, mode):
    # Send byte to data pins
    # bits = data
    # mode = True  for character
    #        False for command

    GPIO.output(LCD_RS, mode) # RS

    # High bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits & 0x10 == 0x10:
        GPIO.output(LCD_D4, True)
    if bits & 0x20 == 0x20:
        GPIO.output(LCD_D5, True)
    if bits & 0x40 == 0x40:
        GPIO.output(LCD_D6, True)
    if bits & 0x80 == 0x80:
        GPIO.output(LCD_D7, True)

    # Toggle 'Enable' pin
    time.sleep(E_DELAY)    
    GPIO.output(LCD_E, True)  
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, False)  
    time.sleep(E_DELAY)      

    # Low bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits & 0x01 == 0x01:
        GPIO.output(LCD_D4, True)
    if bits & 0x02 == 0x02:
        GPIO.output(LCD_D5, True)
    if bits & 0x04 == 0x04:
        GPIO.output(LCD_D6, True)
    if bits & 0x08 == 0x08:
        GPIO.output(LCD_D7, True)

    # Toggle 'Enable' pin
    time.sleep(E_DELAY)    
    GPIO.output(LCD_E, True)  
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, False)  
    time.sleep(E_DELAY)   

"""
Send a string to the LCD display.
"""
def lcd_string(message, style):
    # Send string to display
    # style=1 Left justified
    # style=2 Centred
    # style=3 Right justified

    if style == 1:
        message = message.ljust(LCD_WIDTH, " ")  
    elif style == 2:
        message = message.center(LCD_WIDTH, " ")
    elif style == 3:
        message = message.rjust(LCD_WIDTH, " ")

    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)


###################
# ADDED FUNCTIONS #
###################

""" LCD Options Enum """
class LCDOption(Enum):
    DATETIME = 1
    IP = 2
    FUN = 3

""" Information functions """
def get_ip_address():
    ip_list = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]]
    local_ip_addr = ip_list[0][1]
    return local_ip_addr

def get_date():
    return time.strftime("%a %b %d %Y")

def get_time():
    return time.strftime("%I:%M:%S %Z")

""" Display setters """
def set_display(line1, pos1, line2, pos2):
    lcd_byte(LCD_LINE_1, LCD_CMD)
    lcd_string(line1, pos1)
    lcd_byte(LCD_LINE_2, LCD_CMD)
    lcd_string(line2, pos2)

def display_datetime():
    set_display(get_date(), 1, get_time(), 1)

def display_ip_address():
    set_display("IP Address: ", 1, get_ip_address(), 1)

def display_fun():
    set_display("Fun message!", 2, "Hooray!", 2)

def displayLCDOption(currentOption):
    if currentOption == LCDOption.DATETIME:
        display_datetime()
    elif currentOption == LCDOption.IP:
        display_ip_address()
    elif currentOption == LCDOption.FUN:
        display_fun()
    else:  # default
        display_datetime()

""" Utility """
def next_lcd_option(currentOption):
    next_value = None
    if currentOption == LCDOption.DATETIME:
        next_value = LCDOption.IP
    elif currentOption == LCDOption.IP:
        next_value = LCDOption.FUN
    elif currentOption == LCDOption.FUN:
        next_value = LCDOption.DATETIME
    else:  # default
        next_value = LCDOption.DATETIME
    return next_value
        
########
# MAIN #
########
if __name__ == '__main__':
    leftIsPressed = False
    rightIsPressed = False
    currentOption = LCDOption.DATETIME
    try:
        lcd_init()
        # This sleep is needed or else the LCD messes up from activating too quickly
        time.sleep(2)
        displayLCDOption(currentOption)

        # Listen for button presses
        while True:
            left_button = not GPIO.input(BUTTON_LEFT)
            right_button = not GPIO.input(BUTTON_RIGHT)

            if left_button:
                leftIsPressed = True
            elif leftIsPressed:
                print("Left button pressed - advance to the next LCD view option")
                currentOption = next_lcd_option(currentOption)
                displayLCDOption(currentOption)
                leftIsPressed = False

            if right_button:
                rightIsPressed = True
            elif rightIsPressed:
                print("Right button pressed")
                rightIsPressed = False
            
            # Sleep a bit so we don't hog CPU
            time.sleep(0.2)
    finally:
        GPIO.cleanup()
