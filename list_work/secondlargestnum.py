# write a progrm to find the second largest number in list
num=[1,2,3,4,5,6,7,8,10]

num.sort()

print(num[-2])

largest_num=num[0]

second_largest=num[0]

for i in num:
    print(i)
    if i>largest_num and i >second_largest:

        second_largest=largest_num
        print(second_largest)
        largest_num=i
        print(largest_num)

    elif i> second_largest and i<largest_num:
        second_largest=i


print(second_largest)        

