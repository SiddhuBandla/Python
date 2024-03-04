class Pet():
    name = None 
    fullness = 0
    
    def __init__(self, name):
        self.name= name 
        
    def eat (self, food):
        print(self.name + "is eating" + food )
        if food == "radium ":
            self.fullness = self.fullness +99
        elif food == "Pork":
            self.fullness = self.fullness -99
        elif food == "Chicken Biryani":
            self.fullness = self.fullness +200
        elif food == "bombs":
            self.fullness = self.fullness +20 
        
        print(self.name + ",is now"+ str(self.fullness) +"fullness %")
 
pet_owner_name = input("what is your name?")
print("welcome", pet_owner_name)

pet_1 = Pet("pig")
pet_1.eat("Radium")
