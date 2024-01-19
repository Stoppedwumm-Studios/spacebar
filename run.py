from pyautogui import press, typewrite, hotkey
import time
import tkinter as tk

print("Made by Stoppedwumm-Studios")

print("https://github.com/Stoppedwumm-Studios/spacebar")

def Click():
    clicks = 0
    while clicks < 110:
        press("Space")
        clicks += 1
        time.sleep(0.00001)

window = tk.Tk()
greeting = tk.Label(window, text="Click 120 Times")
schaltf1 = tk.Button(window, text="Do it (:<", command=Click)
credit = tk.Label(window, text="Made by Stoppedwumm-Studios")
site = tk.Label(window, text="https://github.com/Stoppedwumm-Studios/spacebar/")
greeting.pack()
schaltf1.pack()
credit.pack()
site.pack()
window.mainloop()
