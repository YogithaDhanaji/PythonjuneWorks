number=[10,11,12,13,14,15,16,17,18,19,78,42]

# print number of object in number

print(len(number))

# print even number from this number

for i in range (0,len(number)):
    if number [i]%2==0:
        print(number[i])

# print total of number

total=0

for i in range (0,len(number)):
    total=total+number[i]
print(total)


# total number of odd number
odd_total=0

for i in range(0,len(number)):

    if number [i] % 2!=0:
        odd_total+=number[i]

print(odd_total)
        





