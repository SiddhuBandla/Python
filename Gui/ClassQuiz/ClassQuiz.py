from tkinter import *
from tkinter import _ButtonCommand

class QuizStarter: 
    def __init__(self, parent): 
        background_color="Khaki"
        #frame set up
        self.quiz_frame=Frame(parent, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()
        #label widget for the heading 
        self.heading_label=Label(self.quiz_frame, text="Nz Road Quiz", font=("Tw Cen MT","18","bold"),bg=background_color)
        self.heading_label.grid(row=0, padx=20)
        #continue Button

        
    def name_collection(self):
        name=self.entry.box.get()
        name.append(name)
        self.quiz_frame.destroy()
        
        
        
        
        
        
        
        
#start of the prgoram#
if __name__ =="__main__": 
    root = Tk() 
    root.title("NZ Road quiz")
    quiz_instance = QuizStarter(root)
    #To keep the window active 
    root.mainloop() 