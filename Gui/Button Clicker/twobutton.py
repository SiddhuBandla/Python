from tkinter import *

colors = ['red', 'green', 'blue']

window = Tk()
window.geometry("750x1000")

button = Button(window, text="Button1", command=lambda: window.configure(bg=(colors)))

button.pack()

