#write a progarm to print sum of all odd num from 1 to 100

i=1
sum=0

while i<=100:
    if (i%2!=0):
        sum=sum+i

    i=i+1

print(sum)    