# Nested function with calculation

def calculator(a,b):
    def add():
        return a+b
    def multiply():
        return a*b
    print("Sum:",add())
    print("Product:", multiply())
calculator(10,5)

def out():
    x=10
    
    def inn():
        nonlocal x
        x+=5
        
    inn()
    print(x)
    
out()
