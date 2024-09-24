# read start_limit and end limit from user and print all odd number from start_limit and end_limit

start_limit=int(input("enter number"))

end_limit=int(input("enter number"))

i= start_limit

while (i<=end_limit):
    if i%2!=0:
        print(i)

    i+=1
        