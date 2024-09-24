# power ranger

# 2=> 24 [2+22]

# 3=> 369 [3+33+333]


num=int(input("enter number"))

pattern=0

total=0

for i in range (1,num+1):
    pattern=pattern*10+num

    total= total+pattern
print(total)








