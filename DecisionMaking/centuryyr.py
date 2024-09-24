# read a year from user
# print century year if year ends with two zero
# else print non century year

year= int(input("enter year"))

if year%100 ==0:
    print(f"{year} century year")

elif year%100!=0:
    print(f"{year} non century year")


