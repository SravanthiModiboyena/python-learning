
try:  #code inside this block may cause an error.
    with open("no_file.txt", "r") as file: #with ensures the file is automatically closed
        print(file.read()) # read the entire content of the file
except FileNotFoundError: # it excutes only if the file does not exist, prevents program crash.
    print("File not found") 
    
