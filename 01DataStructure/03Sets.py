# set is an unordered collection of unique elements, it is mutable and no duplicates.

# set

print("--------set-------")
s={1, 2, 2, 3, 4, 8} # 1,2,3,4,8
print(s)
print("")

# set methods
'''
   add()-->add elemnts
   update()--> add multiple
   remove()--> remove element
   discard()--> safe remove
   pop()--> remove random
   clear()--> empty set
   copy()--> copy set
   union()--> combines
   intersection()--> common elements
   difference()--> difference
   issubset()--> subset check
   issuperset()--> superset check
   isdisjoint()--> no common 
'''
print("-------set methods-------")

s={1,2,3,4,5,8}
s.add(7)
print(s) # {1,2,3,4,5,7,8}
print("")
s.update([9,10])
print(s) # {1,2,3,4,5,7,8,9,10}
print("")
s.remove(4)
print(s) # {1,2,3,5,7,8,9,10}
print("")
s.discard(12)
print(s) # {1,2,3,5,7,8,9,10}

print("-------set operations-------")

a={1,2,3,4}
b={5,3,6,7}
print("")
print("union()")
print(a.union(b)) #{1,2,3,4,5,6,7}

print("")
print("intersection()")
print(a.intersection(b)) #{3}

print("")
print("difference()")
print(a.difference(b)) # {1,2,4}
print("")
print(b.difference(a)) # {5,6,7}

print("------relation methods------")

print("issubset()")
print("")
s={11,12,13}
x={11,2}
y={12}
print(x.issubset(s)) # false
print("")
print(y.issubset(s)) # true
print("")
print("issuperset()")
print("")
print(s.issuperset(x)) # false
print("")
print(s.issuperset(y)) # true
print("")
print("isdisjoint()")
print("")
t={7,9}
p={20,12}
print(s.isdisjoint(t)) # true
print("")
print(s.isdisjoint(p)) # false 
















