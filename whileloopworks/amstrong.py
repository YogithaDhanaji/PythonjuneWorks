num=int(input("enter number"))

orginal=num

total=0

digit_count=len(str(num))

while num!=0:
    digit=num%10

    exponet=digit**digit_count

    total=total+exponet

    num=num//10

print("amstrong number" if orginal==total else "not armstrong")





    



