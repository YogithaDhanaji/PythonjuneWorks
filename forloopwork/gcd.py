# gcd of (12,24) 

num1=int(input("enter number"))
num2=int(input("enter number"))

gcd=1

for i in range (1,num1+1):
    if num1%i==0 and num2%i==0:
        gcd=i
print(gcd)        




