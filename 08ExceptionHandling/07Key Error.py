# KeyError occurs when key not found in dictionary

try:
    d={"a":1}
    print(d["b"])
except KeyError:
    print("Key not found")


# NameError occurs when variable is not defined

try:
    print(x)

except NameError:
    print("Variable not defined")


# AttributeError

try:
    x=10
    x.append(5)
except AttributeError:
    print("Attribute not found")


