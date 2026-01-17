"""
   * without exception handling program crashes suddenly
   * with exception handling program handles errors gracefully,prevents application failure.

 """

"""
    try:
        # risky code
    except:
        # runs if error occurs
    else:
        # runs if no error
    finally:
        # always runs

"""

try:
    a=10
    b=0
    print(a/b)
except:
    print("Cannot divide by zero")

print("------------------")
try:
    x=int(input("Enter a number: "))
    print(10/x)
except:
    print("Error occurred")
    
