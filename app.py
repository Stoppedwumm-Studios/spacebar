from pyautogui import press, typewrite, hotkey
import time
import tkinter as tk
import os
import threading

print("Made by Stoppedwumm-Studios")

print("https://github.com/Stoppedwumm-Studios/spacebar")

def OpenClick():
    os.system("https://github.com/Stoppedwumm-Studios/spacebar")

def Click():
    clicks = 0
    while clicks < 110:
        press("Space")
        clicks += 1
        time.sleep(0.00001)
        print("CLICK " + str(clicks))

def RunClickThread():
    clickthread = threading.Thread(target=Click, daemon=True)
    clickthread.run()
    return clickthread

print("Defined Clicking")
window = tk.Tk()
greeting = tk.Label(window, text="Click 120 Times")
schaltf1 = tk.Button(window, text="Do it (:<", command=RunClickThread)
credit = tk.Label(window, text="Made by Stoppedwumm-Studios")
site = tk.Label(window, text="https://github.com/Stoppedwumm-Studios/spacebar/")
opensite = tk.Button(window, text="Open Page (Only Windows)", command=OpenClick)
greeting.pack()
schaltf1.pack()
credit.pack()
site.pack()
opensite.pack()
print("Window prepared")
window.mainloop()

print("Window closed")
print("Closing Process")
os.system("echo Done")
