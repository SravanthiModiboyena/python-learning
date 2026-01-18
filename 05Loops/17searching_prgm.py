# Search for a tuple using the loop 

t=(10,20,40,90,50,70)
result=int(input("Enter the element to search: "))

found=False

for i in t:
    if i == result:
        found=True
        break

if found:
    print("Element found in the tuple")
else:
    print("Element not found in the tuple")

    
