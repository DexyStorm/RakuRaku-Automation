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

bad_phrases = ["drift", "drift drive", "drift score", "drift points", "wreckage", "perform", "wrecking", "skill points", "perform near - miss", "near-miss"]



def check_auto_drive(text: str):

	if("enable auto drive" in text.lower()):
		keyboard.press('c')
		keyboard.release('c')
		time.sleep(1)
		keyboard.press('2')
		keyboard.release('2')


def reset_job():
	
	time.sleep(15)
	
	keyboard.press(Key.esc)
	keyboard.release(Key.esc)
	
	time.sleep(2)
	
	keyboard.press(Key.right)
	keyboard.release(Key.right)
	
	time.sleep(2)
	
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	
	time.sleep(1)
	
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	
	time.sleep(15)
	
	keyboard.press("m")
	keyboard.release("m")
	
	time.sleep(2)
	
	keyboard.press("a")
	keyboard.press("s")
	time.sleep(3)
	keyboard.release("a")
	time.sleep(3)
	keyboard.release("s")

	keyboard.press(Key.up)
	time.sleep(2)
	keyboard.release(Key.up)

	keyboard.press("w")
	time.sleep(5.41)
	keyboard.release("w")

	keyboard.press("d")
	time.sleep(0.135)
	keyboard.release("d")

	keyboard.press("x")
	keyboard.release("x")

	time.sleep(2)

	keyboard.press(Key.enter)
	keyboard.release(Key.enter)

	time.sleep(15)


def check_bad_phrases(text):
	for each_bad_phrase in bad_phrases:
		if(each_bad_phrase in text.lower()):
			reset_job()
			break

def screen_scanning():

	keyboard.press('c')
	keyboard.release('c')
	time.sleep(1)
	
	screenshot = pyautogui.screenshot()
	keyboard.press('c') # these 2 lines must be here cuz python is a piece of shit
	keyboard.release('c') # these 2 lines must be here cuz python is a piece of shit

	text = pytesseract.image_to_string(screenshot) #first, simple version

	check_auto_drive(text)
	check_bad_phrases(text)

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