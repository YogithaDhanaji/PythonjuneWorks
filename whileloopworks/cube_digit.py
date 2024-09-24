# sum of cube of each digit

# 543

#5^3 +4^3+3^3

num=int(input("enter number"))


sum=0

while num!=0:
    digit=num%10

    exponent=digit**3

    sum=exponent+sum

    num=num//10

print(sum)    




