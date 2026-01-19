'''
   File handling it is creating,opening,reading,writing,updating,and closing files

   files are used to store data permanently,read large data  
'''

# syntax: open(filename, mode)

file=open(r"C:\Users\mskri\Downloads\python-learning\05Loops\00basics Loops.py","r")

print(file.read())
file.close()

