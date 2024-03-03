from tkinter import *

window = Tk()

def open_command():
    open_btn.config(bg='green')
    close_btn.config(bg='white')

def close_command():
    open_btn.config(bg='white')
    close_btn.config(bg='red')

font=('Times New Roman', 12)
open_btn = Button(window, text='Open', font=font, fg='green', bg='white', width=5, command=open_command)
open_btn.pack()
close_btn = Button(window, text='Close', font=font, fg='red', bg='white', width=5, command=close_command)
close_btn.pack()

window.mainloop()