# Imports tkinter for GUI.
from tkinter import *

# Starts the student class.
class Student:

    def __init__(self, name):
        self.name = name

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

    def display_name(self):
        print(self.first_name)
    
def show_grade():
    # Show grade using a label.
    grade_label.config(text=csc_2[0].get_grade())

# Starts the dictionary with currently no students.
csc_2 = []

csc_2.append(Student("Aaran", "Excellence"))
csc_2.append(Student("Hamish", "Meritorious"))
csc_2.append(Student("Gabby", "Achievement"))

window = Tk()
window.geometry("300x300")

# Sets up listbox.
students_listbox = Listbox(window)
students_listbox.pack()

students_listbox.insert(0, "Aaran.")
students_listbox.insert(1, "gabby.")

# Sets up grade label.
grade_label = Label()
grade_label.pack()

# Show grade button.
show_grade_btn = Button(text="Show Grade.", command=show_grade)
show_grade_btn.pack()

window.mainloop()