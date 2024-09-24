num1=100

num2=200

# write a progam to swap two numbers

# values before swapping num1=100 num=200
# values after swapping num1=200 num2=100

print(f"values before swaping num1={num1} num2={num2}")
# temp logic:1
# temp=num1 #temp=100
# num1=num2 #num1=200
# num2=temp #num2=100

print(f"value after swapping num1={num1} num2={num2} ")

# addition logic:2
# num1=num1+num2 #100+200=300
# num2=num1-num2 #300-200=100
# num1=num1-num2 #300-100=200

print(f"value after swapping num1={num1} num2={num2}")

#logic only used in python

(num1,num2)=(num2,num1)

print(f"value after swapping num1={num1} num2={num2}")
