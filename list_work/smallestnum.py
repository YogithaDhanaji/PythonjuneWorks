num=[0,3,4,5,6,7,8,10]

smallest_num=num[0]

for i in num:
    if i <smallest_num:

        smallest_num=i

print(smallest_num)        

# SECOND SMALAEST

num.sort()

smallest_number=num[0]

sec_smallest=num[-1]

for i in num:
    print(i)
    if i<sec_smallest and i<smallest_number:
        sec_smallest=smallest_number
        smallest_number=i

    elif i<sec_smallest and i>smallest_num:
        sec_smallest=i
        
print(sec_smallest)        