# Operators are used to perform operations on values and variables.

# Operators in Python
# 1. Arithmetic Operators : +, -, *, /, %, //, **
# 2. Relational(Comparison) Operators : ==, !=, >, <, >=, <=
# 3. Logical Operators : and, or, not
# 4. Bitwise Operators : &, |, ~, ^, <<, >>
# 5. Assignment Operators : =, +=, -=, *=, /=, %=, //=, **=
# 6. Identity Operators : is, is not
# 7. Membership Operators : in, not in
# 8. Ternary Operator : [on_true] if [expression] else [on_false]
# 9. Operator Precedence : BODMAS : Brackets, Orders, Division, Multiplication, Addition, Subtraction
# 10. Operator Overloading : + operator is used for addition and concatenation
# 11. Operator Functions : add, sub, mul, truediv, floordiv, mod, pow
# 12. Special Operators :  __add__, __sub__, __mul__, __truediv__, __floordiv__, __mod__, __pow__

# arithmetic operators

print("----Addition----")
a=10
b=5
print(a+b) #15

print("----substraction----")
print(a-b) # 5

print("----Multiplication----")
print(a*b) # 50

print("----Division----")
print(a/b) # 2.0

print(b/a) # 0.5

print("----modulus----")
print(a%b) #0
print(b%a) #5

print("----exponent----")
print(a**b) # 100000
print(b**a) # 9765625

print("----floor division----")
print(a//b) # 2
print(b//a) # 0

# Relational Operators

print("--Relational Operators--")
a=10
b=20
print(a==b) # False
print(a!=b) # True
print(a>b) # False
print(a<b) # True
print(a>=b) # False
print(a<=b) # True

#Logical Operators

print("---Logical Operators---")
a=10
b=5
print(a>5 and b<10)
print(a<5 or b<10)
print(not(a>5))











