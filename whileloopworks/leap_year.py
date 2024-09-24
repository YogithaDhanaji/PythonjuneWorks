# print all leapyear from 1800 to 2024

year=1800

while year<=2024:
    if (year%400==0 and year%100==0) or (year%4==0 and year%100!=0):

        print(year)

    year+=1   


