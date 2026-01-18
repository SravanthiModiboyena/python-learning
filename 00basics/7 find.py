# find() it returns the index of the first occurence of the substring.
# if the substring is not found, it returns -1(no error). it works for strings only.
''' syntax

    string.find(substring)
    string.find(substring, start, end)

'''

print("Python is a programming language")
str="Python is a programming language"
print("")
print(str.find("programming"))


# example: not found

print("I love to learn new things very much")
str="I love to learn new things very much"
print(str.find("Z")) # -1 no error is raised


# example: start & end

print("Banana") 
str1="Banana"
print(str1.find("a",4))# the first "a" starting from index 4 is the one at index 5         
      

