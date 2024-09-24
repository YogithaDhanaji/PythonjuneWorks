# class list

    #       def append/add element to the end of the list
    #       deg insert()/add element to spesific position
    #       def count() /
    #       def pop()  / remove last element and return the element
    #       def remove()


num=[1,1,2,3,4]
num.append(5)
print(num)

num.insert(1,6)
print(num)

print(num.count(6))

print(num.pop()) # remove the last element and return it

print(num.pop(2)) # remove the item in index 2 and return value
print(num)

num.remove(1)  # remove the spesific element in the list in the first occurence

print(num)

num.extend([5,6,7,8,9])  # add a collection of element to a list


print(num)

