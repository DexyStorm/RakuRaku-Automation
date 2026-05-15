from pynput.keyboard import Key, Controller
import time
import pyautogui
import pytesseract



###
# YOU CAN ADJUST THE VARIABLES THAT ARE IN-BETWEEN THE #
check_auto_drive_on_iteration = 2 # how many iterations need to happen untill it checks if auto-drive has been turned off
###


def check_auto_drive():

	keyboard.press('c')
	keyboard.release('c')
	time.sleep(1)
	
	screenshot = pyautogui.screenshot()

	text = pytesseract.image_to_string(screenshot)
	# print(text)
	
	if("enable auto drive" in text.lower()):
		#print("auto drive not turned on. trying to turn it on...")
		keyboard.press('c')
		keyboard.release('c')
		time.sleep(1)
		keyboard.press('2')
		keyboard.press('2')


if __name__ == "__main__":

	keyboard = Controller()
	i = 0

	while(True):
		i = i + 1
		time.sleep(5)

		keyboard.press(Key.enter)
		keyboard.release(Key.enter)

		if(i == check_auto_drive_on_iteration - 1):
			
			check_auto_drive()
			i = 0