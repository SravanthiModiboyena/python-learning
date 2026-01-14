'''format()method is used to insert values into a string in readable way'''

#Example
name="Python"
print("Welcome to {}".format(name))

#multiple values
name="Shasra"
age=23
print(("My name is {}\nMy age is {}").format(name,age))

#Positional index
print("I like {0} and {1}".format("Python","Java"))

print("I like {1} and {0}".format("Python","Java"))

#Formatting Percent

value=0.85
print("Sucess rate:{:.0%}".format(value))
