# set=={"",""} or set()

name={"yogi","tha","hello"}

new_name={"hp","rain","sum","hello"}

# print(type(nume))

# s=set()
# print(type(s))
# print(nume)

# no duplicates
# no index position
# no oder
# mutable we can add or remove element from  set

# nume.add("kochi") # add elelment to set object
# print(nume)
# nume.clear() # remove all element from object ,empty set remains
# print(nume)
# nume.pop() # remove random element
# print(nume)

# name.discard("hello")  # remove an element frome the set if it is a member in the object

# print(name)

# name . update(new_name)  #add the  element any collection of the set

# print(name)
# union 
# intersection
# difference
new_set=name.union(new_name) # return the combined element from two set and return as a new 
print(new_set)
new_set=name.intersection(new_name) #return the common element from 2 set object as a new set

print(new_set)
new_set=name.difference(new_name) #return element from set name which is not in new set as new set

print(new_set)

new_set=name.symmetric_difference(new_name)  #combine all element from 2 set and remove common elements
print(new_set)