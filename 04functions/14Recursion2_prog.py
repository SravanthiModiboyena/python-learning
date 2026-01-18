#Recursion: A function calling itself to solve a problem
'''
   Every recursive function must have:

   Base case: --> stops recursion
   Recursive Case: --> function calls itself
   
'''

'''
    Syntax:

    def func_name():
        if base_condition:
            return value
        else:
            return
    func_nmae(prblm)
'''


# Factorial of a number

# formula n!=n*(n-1)!

def factorial(n):
    if n==0: #Base case
        return 1
    return n * factorial(n-1) # Recursive case

print(factorial(5))

        
             
