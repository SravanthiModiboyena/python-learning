#FileNotFoundError occurs when files does not exist

try:
    file = open("data.txt","r")

except FileNotFoundError:
    print("File not found")
    
