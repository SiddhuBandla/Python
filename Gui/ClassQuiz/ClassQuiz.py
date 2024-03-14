from tkinter import *
import random

names = []
global questions_answers
asked=[]
score=0

questions_answers = {
    1: ["What must you do when you see blue and red flashing lights behind you?", 'Speed up to get out of the way', 'Slow down and drive carefully', 'Slow down and stop', 'Drive on as usual', 'Slow down and stop',3],
    
    2: ["You may stop on a motorway only:", 'if there is an emergency', 'to let down or pick up passengers', 'to make a U-turn', 'to stop and take a photo', 'if there is an emergency',1],
    
    3: ["When coming up to a pedestrian crossing without a raised traffic island, what must you do?", "Speed up before the pedestrians cross", 'Stop and give way to pedestrians on any part of the crossing', "Sound the horn on your vehicle to warn the perestrians", "slow down to 30knh", 'Stop and give way to pedestrians on any part of the crossing',2],
    
    4: ["Can you stop on a bus stop in a private motor vehicle?", "Only between midnight and 6am", "Under no circumstances", 'When dropping off passengers', 'Only if it is less than 5 minutes', 
        "Under no circumstances", 2],
    
    5: ["What is the maximum speed you may drive if you have a 'space saver wheel' fitted? (km/h)", '70 km/h', "100 km/h so you do not hold up traffic", "80 km/h and if the wheel spacer displays a lower limit that applies", "90 km/h", "80 km/h and if the wheel spacer displays a lower limit that applies",3],
    
    6: ["When following another vehicle on a dusty road, you should:", 'Speed up to get passed', "Turn your vehicle's windscreen wipers on", "Stay back from the dust cloud", 'Turn your vehicles headlights on', "Stay back from the dust cloud",3], 
    
    7: ["What does the sign containing the letters 'LSZ' mean", "Low safety zone", "Low stability zone", "Lone star zone", "Limited speed zone", 'Limited speed zone',4], 
    
    8: ["What speed are you allowed to pass a school bus that has stopped to let students get on or off?", "20 km/h", "30 km/h", "70 km/h", '10 km/h', '20 km/h',1], 
    
    9: ["What is the maximum distance a load may extend in front of a car?", '2 meters forward of the front edge of the front seat',
"4 meters forward of the front edge of the front seat", "3 meters forward of the front edge of the front seat", '2.5 meters forward of the front edge of the front seat', '3 meters forward of the front edge of the front seat',3],
    
    10:["To avoid being blinded by the headlights of another vehicle coming towards you what should you do?", "Look to the left of the road", 'Look to the centre of the road', 'Wear sunglasses that have sufficient strength', 'Look to the right side of the road', 'Look to the left of the road',1],
}

def randomiser(): 
    global qnum
    qnum = random.randint(1,10)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()

randomiser()

class QuizStarter:
    def __init__(self, parent):
        
        background_color="Oldlace"

        self.quiz_frame=Frame(parent, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        self.heading_label = Label(self.quiz_frame, text="NZ Road Rules", font=("Tw Cen MT", "18", "bold"), bg= background_color)
        self.heading_label.grid(row=0)

        self.user_label=Label(self.quiz_frame, text="Please enter your username below: ", font=("Tw Cen MT", "16"), bg=background_color)
        self.user_label.grid(row=1, pady=20)

        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2, pady=20)

        self.continue_button = Button(self.quiz_frame, text="Continue", font=("Helvetica", "13", "bold"), bg="orange", command=name_collection)
        self.continue_button.grid(row=3, pady=20)

        self.question_label=Label(self.quiz_frame, text=questions_answers[qnum][0], font=("Tw Cen MT", "16"),bg=background_color)
        self.question_label.grid(row=1, padx=10, pady=10)

def name_collection(self):
    name=self.entry_box.get()
    names.append(name)
    self.quiz_frame.destroy()
    Quiz(root)

class Quiz:
        def __init__(self, parent):
            
            background_color="Oldlace"
            
            self.quiz_frame=Frame(parent, bg = background_color, padx=40, pady=40)
            self.quiz_frame.grid()
            
            self.question_label = Label(self.quiz_frame, text=questions_answers[qnum][0], font=("Tw Cen MT", "18"), bg= background_color)
            self.question_label.grid(row=0, padx=10, pady=10)
            
            self.var1 = IntVar()

            #radio button 1
            self.rb1= Radiobutton(self.quiz_frame, text=questions_answers [qnum][1], font=("Helvetica", "12"), bg=background_color, value=1, padx=10, pady=10, 
                              variable=self.var1, indicator = 0, background = "light blue") 
            self.rb1.grid(row-2, sticky-W)
            
            # radio button 2
            self.rb2= Radiobutton(self.quiz_frame, text=questions_answers [qnum][2], font=("Helvetica", "12"), bg=background_color,value=2,padx=10, pady=10, 
                             variable=self.var1, indicator = 0, background = "light blue")
            self.rb2.grid(row=3, sticky=w)
            
            #radio button
            self.rb3= Radiobutton(self.quiz_frame, text= questions_answers[qnum][3], font=("Helvetica", "12"), bg=background_color, value=3, padx=10, pady=10, 
                              variable=self.var1, indicatorc= 0, background = "light blue") 
            self.rb3.grid(row=4, sticky=W)
            
            # radio button 4
            self.rb4= Radiobutton(self.quiz_frame, text=questions_answers[qnum][4], font=("Helvetica","12"), bg=background_color, value=4, padx=10, pady=10, 
                              variable=self.var1, indicator = 0, background = "light blue") 
            self.rb4.grid(row=5, sticky=W)
            
            #confirm button
            self.quiz_instance= Button(self.quiz_frame, text="Confirm", font=("Helvetica", "13", "bold"), bg="SpringGreen3")#, command=self.test_progress) self.quiz_instance.grid(row=7, padx=5, pady=5)
            
            #score label        
            self.score_label=Label(self.quiz_frame, text="SCORE", font=("Tw Cen MT", "16"), bg=background_color,) 
            self.score_label.grid(row=8, padx=10, pady=1)

randomiser()

if __name__ == "__main__":
    root = Tk()
    root.title("NZ Road Rules Quiz")
    quiz_instance = QuizStarter(root)
    root.mainloop()