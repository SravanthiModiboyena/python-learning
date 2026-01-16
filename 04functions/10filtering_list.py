
# filter(): This function filters the elements of an iterable based on a function.

'''
   Syntax :

   filter(function, iterable)

   function --> it returns True or False
   iterable --> list,tuple,set,
   
   
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def even_numbers(n):
    return n % 2 == 0

result = list(filter(even_numbers, numbers))

print(result)

# filter with lambda

even_numbers = list(filter(lambda x : x <= 20, numbers))

print(even_numbers)
