# nested function is a function defined in another function called outer function in inner function

def outer():
    print("This is outer function")

    def inner():
        print("This is inner function")
    inner() #this is inner function
outer() #this is outer function


# inner function using outer variable

def srav(name):
    def ammu():
        print("Hello",name)
    ammu()
srav("Shasra") # Hello Shasra

# Returning inner function

def message(msg):
    def greet():
        print(msg)
    return greet
result =message("Welcom to Python-learning")
result()

