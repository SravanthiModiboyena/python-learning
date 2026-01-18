# index() with string

animals="I wake up early in the morning"
print(animals.index("g"))  # index() is used to find the position()of a value in a sequence
print(animals.index("r"))  #index() it returns the first index where the specified value is found.
print(animals.index("a"))   
print(animals.upper()) # makes all to upper case
print(animals.lower()) # makes all to lower cases
print(animals.strip()) # clears the white spaces
print("dog horse tiger deer".count("e")) #count the char presented number of times
print("animals".count("e"))
print("...".join(["dog","horse","tiger","deer"]))

# index() with list

print("--------index-------")
print("")
numbers=[10,20,30,40,10]
print(numbers.index(30)) # finds first occurance only


# index() with tuple

print("--------index-------")
print("")
t=(1,2,9,7,6)
print(t.index(9))


 
