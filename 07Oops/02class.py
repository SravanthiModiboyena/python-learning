class Student:
    def __init__(self,name,age): # we use __init__() to automatically initialize(assign)values to an object when it is created
        self.name=name
        self.age=age
        
s1=Student("SKY",25)
s2=Student("Sravs",24)
s3=Student("Sam", 9)

print(s1.name,s1.age)
print(s2.name,s2.age)
print(s3.name,s3.age)


