name=input("Enter a name: ")

with open("names_file.txt","a") as file:
    file.write(name)
