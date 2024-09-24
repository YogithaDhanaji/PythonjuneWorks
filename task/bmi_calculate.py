height_in_cm=int(input("enter height"))

weight_in_kg=int(input("enter weight"))

height_in_m=height_in_cm/100

BMI=weight_in_kg/(height_in_m**2)

print(f"{BMI}")

if BMI<=19:
    print(f"under weight")

elif BMI>=19 and BMI>=25:
    print(f"normal weight")

elif BMI>=25 and BMI<=30:
    print(f"over weight")

else:
    print("obesity")    
