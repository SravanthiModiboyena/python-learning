'''
   Conditional Statements allows a program to make decisions based on conditions.

   python executes different blocks of code depending on whether a condition is True or False.

   Types of conditional statements in python -->if
                                             -->if-else
                                             -->if-elif-else
                                             -->nested if

   The if statement is used to execute a block of code if the condition is True.

   The else statement is used to execute a block of code if the condition is False.
   The elif statement is used to execute a block of code if the condition is True, and the previous conditions are False.
   The pass statement is used to avoid getting an error.
   The nested if statement is used to execute a block of code if the condition is True, and the previous condition is True.
   The one-line if statement is used to execute a block of code if the condition is True.
   The one-line if-else statement is used to execute a block of code if the condition is True, and the previous condition is False.
   The one-line if-elif-else statement is used to execute a block of code if the condition is True, and the previous conditions are False.

'''

print("--if statement--")
age=18

if age >=18:
    print("Eligible for vote")

print("--if-else statement--")

if age>=18:
    print("Eligible")
else:
    print("Not eligible")

print("--if-elif-else--")

marks=92

if marks>=90:
    print("Grade A") 
elif marks >=75:
    print("Grade B")
elif marks >=60:
    print("Grade C")
else:
    print("Student Fail")

#nested if (if inside another if)
    
print("--nested if statement--")
username="Shasra"
password="Password"

if username=="Shasra":
    if password == "Shasra99@":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Wrong Username")










