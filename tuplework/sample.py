# num=(1,2,3,4) # tuple defined by()

# print(num[2]) # index position ,duplicate allow, immutable,index(),cont()

numbers=[1,2,[3,(100,200,300),4],5,6]

num=numbers[2][1]

new_number=list(num)

new_number.append(500)

numbers[2][1]=tuple(new_number)

print(numbers)