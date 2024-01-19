from pyautogui import press, typewrite, hotkey
import time
import tkinter as tk

clicks = 0
def Click():
    while clicks < 110:
        press("Space")
        clicks += 1
        time.sleep(0.00001)

window = tk.Tk()
schaltf1 = tk.Button(window, text="Aktion durchführen", command=Click)
schaltf1.pack()
window.mainloop()        
