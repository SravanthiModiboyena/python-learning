# Variable-Length Arguments(*args)

#used when you don't know how many arguments will be passede.

def total(*numbers):
    sum=0
    for n in numbers:
        sum+=n
    return sum
print(total(10,20,30))
print(total(5,10))

# *args stores values as a tuple

def calc_avg(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum/len(args)
print(calc_avg(10, 20, 20))          # this will print the avg the given arguments 
print(calc_avg(10, 10, 20, 30))      # this will print the avg the given arguments
