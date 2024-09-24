number=int(input("enter number"))

previous=0

current=1

next=previous+current

isfibo=False

if number in (0,1):
    isfibo=True

else:
    next= previous+current


    while (next<=number):
        next=previous+current

        previous=current

        current=next

        if next==number:
            isfibo=True

            break

print(isfibo)








