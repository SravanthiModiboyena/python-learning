'''
  Loop is used to repeat a block of code multiple times without writing code again and again.
  Repeat tasks until a condition is met .

'''


#  for loop it is used to iterate over a sequence.
#  The number of iterations is fixed or predictable.
#  for loop is best for Lists, String, Tuples, Dictionaries, Ranges


# for loop Example 1 Print numbers 
print("--------Numbers-------")
for i in range(0, 5):
    print(i,"\n")
    
# Example 2 loop through a list
print("---------List---------")
fruits = ["Apple", "Berry","Cherry"]

for fruit in fruits:
    print("\n", fruit)

# Example 3 loop through String

print("\n","-----String------")
for ch in "Python":
    
    print(ch)

# while loop it repeats the code as long as condition is true

# example 1

i=1
print("\n"," Print Numbers")
print("-----------------")
while i<=5:
    print(i)
    i+=1

i=10
print ("\n","Print Numbers")
print("-------------------")
while i>=5:
    print(i)
    i-=1

#  break statement it stops the loop immediately

print("-------Break--------")
for i in range(1,10):
    if i==5:
        break
    print(i)

# continue Statement it skips the current iteration and moves to the next one

# example Skip number 5

print("------continue-------")
for i in range(1,8):
    if i==5:
        continue
    print(i)


# pass Statement it does nothing well it is used as a placeholder

# example

print("-------pass-------")
for i in range(3):
    pass
    print(i) 

# else with loop it runs only if the loop completes normally (No breaks)

# example else runs

print("--------else runs--------")
for i in range(3):
    print(i)
else:
    print("Loop finished")


# example for else does not run

print("--------else does not run--------")
for i in range(1,5):
    if i ==3:
        break
    print(i)
else:
    print("Completed")



























