#0 1 1 2 3 5 8 

previous=0

current=1

print(f"{previous},{current}",end=",")

for i in range (1,11):
    next=previous+current

    print(F"{next}",end=",")


    previous=current

    current=next


    