'''
   syntax :

   def decorator(func):
       def wrapper():
           func()
       return wrapper
       
'''

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
        return "done" 
    return wrapper
@my_decorator
def greet():
    print("Hello")
    print("world")
print(greet())
def add(a,b):
    return a+b
print(add(3,8))
    
