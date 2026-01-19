# Dictionary is a collection of data stored as key-value pairs

this_dict = {'names':['chenchu',"reddy",'siva', 'krisna','rajia','sai'],
             'age':[23, 24, 25, 26, 27, 28],
            'height':[5.6, 5.7, 5.8, 5.9, 6.0, 6.1],
            'weight':[60, 70, 80, 90, 100, 110]}
#print(this_dict)

print(this_dict['names'])
print("")
print("Keys in the dictionary:")
print(this_dict.keys())
print("")
print("Values in the dictionary:")
print(this_dict.values())
print("")
print("Items in the dictionary:")
print(this_dict.items())
print("")
print(len(this_dict))
print("")
print(len(this_dict['names']))
print("")
print(type(this_dict))
print("")
this_dict.update({'names':['Ram',"Bheem",'Lava', 'Kusa','Daana','Veera']})
print("")
print(this_dict['names'])
print("")
print(this_dict)
print("")
print(this_dict.get('names'))
print("")
print(this_dict.pop('names'))
print("")
print(this_dict)
print("")
this_dict['cities']=('Hyderabad','Bangalore','Chennai','Mumbai','Delhi','Kolkata')
print("")
this_dict.update({'states':['Telangana','Karnataka','Tamilnadu','Maharashtra','Delhi','West Bengal']})
print("")
print(this_dict)
print("")
print(this_dict.keys())
print("")

# this_dict.update() --> add new key-value pairs
# this_dict.pop() --> removes specific key
# this_dict.clear() --> it removes all items
# this_dict.get()--> it get a value using key
# this_dict.keys()--> it returns all keys
# this_dict.values()--> it retruns all values
# this_dict.items()--> it returns key-value pairs
# this_dict.popitem()--> it removes the last inserted item
# this_dict.copy()--> it creates a shallow copy
# len(this_dict)--> returns number of items
# type(this_dict)--> it retruns data type of a dict.
# del dict[key]--> it delete a key 

























