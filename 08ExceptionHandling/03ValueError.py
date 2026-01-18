#value error when wrong type of value is given it occurs

try:
    x = int("abc")
    print(x)
except ValueError:
    print("Invalid value")

    
