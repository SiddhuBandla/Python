from tkinter import *


class Student:
    
    def __init__(self, name, grade):
        self.name = name 
        self.grade = grade
    
    def get_grade(self):
        return self.grade 
        
    def set_grade(self, grade):
        self.grade = grade 


def show_grade():
    selected_index = students_listbox.curselection()[0]
    student = csc_2[selected_index]
    grade_label.config(text=student.get_grade())


csc_2 = []

csc_2.append(Student("Aaran", "Excellence"))
csc_2.append(Student("Hamish", "Meritorious"))
csc_2.append(Student("Gabby", "Achievement"))

window = Tk()
window.geometry("500x500")

students_listbox = Listbox(window)
students_listbox.pack()

for student in csc_2:
    students_listbox.insert(END, student.name)

grade_label = Label()
grade_label.pack()

show_grade_btn = Button(text="Show Grade", command=show_grade)
show_grade_btn.pack()

window.mainloop()
