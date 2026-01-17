

class Person:
    def __init__(self, age):
        if age <= 0:
            self.age = 0
            print("Age is not valid, setting age to 0")
        else:
            self.age = age

    def yearPasses(self):
        self.age += 1
        
    def howOld(self):
        
        if self.age < 13:
            print("You are young.")
            
        elif 13 <= self.age <18:
            print("You are a teenager.")
            
        else:
            print("You are old.")

age=int(input("Enter your age:"))
p=Person(age)
p.howOld()
p.yearPasses()
 
