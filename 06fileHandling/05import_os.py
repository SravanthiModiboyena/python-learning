import os

file_path=os.path.join(os.getcwd(),"names.txt")

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        print(file.read()) #reads the entire file
else:
    print("File not found")


# os module --> works with os paths
# getcwd() --> gets current working directory
# path.join() --> safe path creation
# read() --> reads full file 
