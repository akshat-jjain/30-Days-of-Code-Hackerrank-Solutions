class Person:
    age=0
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        
        if initialAge<0:
            print("Age is not valid, setting age to 0.")
            self.age=0
        elif initialAge>0:
            self.age=initialAge
    def amIOld(self):
        
        if 13>self.age:
            print("You are young.")
        elif 13<=self.age<18:
            print("You are a teenager.")
        elif self.age>=18:
            print("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here
        self.age+=1
