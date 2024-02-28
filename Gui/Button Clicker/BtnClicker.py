from tkinter import *

click_count = 0

def btn_click():
    global click_count
    click_count += 1
    print("number of clicks", click_count)

window = Tk()

btn= Button(window, text="click me!", command=btn_click)

btn.pack()

window.mainloop()
