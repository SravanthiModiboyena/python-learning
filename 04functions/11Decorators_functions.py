# Decorators : A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.

# syntax : def decorator_function(func):

def my_decorator(func):
    def wrapper(): # wrapper it wraps the original function with extra logic without changing its code.
                   # wrapper() is an inner function that wraps another function to extend or modify its behavior. 
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")

decorated_hello = my_decorator(say_hello)
decorated_hello()

# In this example : my_decorator is a decorator function. It takes say_hello function as an argument and extends its behavior.

# The wrapper function is the decorator function. It takes say_hello function as an argument and extends its behavior.
print("------my decorator-------")

@my_decorator
def say_goodbye():
    print("Goodbye!")

say_goodbye() # This is equivalent to say_goodbye = my_decorator(say_goodbye), but more readable and commonly used.

# In this example : @my_decorator is a decorator. It takes say_goodbye function as an argument and extends its behavior.
