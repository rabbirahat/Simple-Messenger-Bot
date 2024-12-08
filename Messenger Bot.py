import pyautogui
import time
message = 3
while message > 0:
    time.sleep(3)  #waits 3 sec
    pyautogui.typewrite('Hello, There! How are you?')
    time.sleep(2)
    pyautogui.press('enter')
    message = message - 1
