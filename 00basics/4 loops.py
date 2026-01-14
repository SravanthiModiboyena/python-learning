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



