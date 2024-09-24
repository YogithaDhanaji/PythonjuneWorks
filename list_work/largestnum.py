# write a program to find the largest num without using method


num=[1,2,3,4,5,6,7,8,10]

# num.sort()

# print(num[-1])

largest_num= num[0]

for i in num:
    if i>largest_num:
        largest_num=i
print(f"largest number is {largest_num}")

