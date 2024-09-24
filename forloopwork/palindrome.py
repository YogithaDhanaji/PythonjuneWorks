#write a program to chk number is palindrome or not

# 121is palindromic number 

#123 is not palindromic number 

num=int(input("enter number"))

result=0

original=num

while num!=0:

    digit=num%10

    num=num//10

    print(digit) 

    result=result*10+digit

print(result)    

print("palindrome"if result==original else "non palindrome")


    









