# Reverse a number

num=1234
reverse=0

while num>0:
    digit = num%10 # %modulus gives the last digit of the number 
    reverse = reverse * 10 + digit # reverse * 10 it shifts digits left 
    num//=10 #removes the last digit from num uses floor division
print(reverse)
