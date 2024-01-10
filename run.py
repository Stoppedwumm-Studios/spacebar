from pyautogui import press, typewrite, hotkey
import time

clicks = 0

while clicks < 110:
    press("Space")
    clicks += 1
    time.sleep(0.00001)        