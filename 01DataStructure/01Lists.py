# List

print("-------list-------")
numbers = [10,20,30,40,50]
print(numbers[0]) #10
print(numbers[-1]) #40
print(numbers[-2]) #30

# list Methods

'''
   append() --> add element
   insert() --> add new element at position
   remove() --> remove value
   pop() --> remove by index
   sort() --> sort list
   reverse() --> reverse list
   index() --> find index
   count() --> count occurrences
   clear() --> remove all elements
   extend() --> add multiple values
   
   
'''
print("------list methods------")
numbers.append(70)
print(numbers) # 10, 20, 30, 40, 50, 70
numbers.insert(2, 90)
print(numbers) # 10, 20, 90, 30, 40, 50, 70
numbers.remove(10)
print(numbers) # 20, 90, 30, 40, 50, 70
numbers.pop()
print(numbers) # 20, 90, 30, 40, 50
numbers.sort()
print(numbers) # 20, 30, 40, 50, 90
numbers.reverse()
print(numbers) # 90, 50, 40, 30, 20
print(numbers.index(50)) # 1
print(numbers.count(40)) # 1
print(numbers.clear()) # none
numbers.clear()
print(numbers) # []
numbers.extend([100,200,300])
print(numbers) # [100, 200, 300]













