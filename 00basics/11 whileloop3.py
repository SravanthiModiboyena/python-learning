
# user input

password =""

while True:
    password = input("Enter password:")

    has_alpha = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isalpha():
            has_alpha = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_special = True

    if has_alpha and has_digit and has_special:
        print("Access Granted")
        break
    else:
        print("Access denied: Password must contain alphabets, numbers, and special characters")


