'''# infinte loop

i=1
while i>0:
    print(i)
    
#break
'''
# using break 

i=1
while i <= 10:
    if i == 9:
        break
    print(i)
    i += 1


# using continue

print("------continue-------")
i=0
while i<5:
    i+=1
    if i==3:
        continue
    print(i) 


