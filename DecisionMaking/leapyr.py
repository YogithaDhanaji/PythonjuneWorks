# write a program to check year is leap year or not

year=int(input("enter year"))

if (year%100==0 and year%400==0) or (year%100 !=0 and year%4==0):

    print(f"{year} is leap year")

else:

    print("not leap year")


