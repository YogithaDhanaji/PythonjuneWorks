weight_in_kg=int(input("enter weight"))

height_in_cm=int(input("enter cm"))

height_in_meter=height_in_cm/100

bmi=weight_in_kg/(height_in_meter**2)

print(f"bmi is {bmi}")

if bmi<=19:
    print(f"under weight")

elif bmi>=19 and bmi>=25:
    print(f"normal weight")

elif bmi>=25 and bmi<=30:
    print(f"over weight")

else:
    print("obese")
        

