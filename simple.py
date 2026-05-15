from pynput.keyboard import Key, Controller
import time
import pyautogui
import pytesseract
import cv2
import numpy



###
# YOU CAN ADJUST THE VARIABLES THAT ARE IN-BETWEEN THESE #
screen_scanning_timer = 2 # how many iterations need to happen until the program takes a screenshot of the monitor and scans it
###


def check_auto_drive(text: str):

	if("enable auto drive" in text.lower()):
		keyboard.press('c')
		keyboard.release('c')
		time.sleep(1)
		keyboard.press('2')
		keyboard.release('2')


def screen_scanning():

	keyboard.press('c')
	keyboard.release('c')
	time.sleep(1)
	
	screenshot = pyautogui.screenshot()
	keyboard.press('c') # these 2 lines must be here cuz python is a piece of shit
	keyboard.release('c') # these 2 lines must be here cuz python is a piece of shit

	text = pytesseract.image_to_string(screenshot) #first, simple version

	check_auto_drive(text)
	

if __name__ == "__main__":

	keyboard = Controller()
	i: int = 0

	while(True):
		i = i + 1
		time.sleep(5)

		keyboard.press(Key.enter)
		keyboard.release(Key.enter)

		if(i == screen_scanning_timer - 1):
			
			screen_scanning()
			
			i = 0