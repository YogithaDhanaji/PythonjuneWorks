#write a program to calculate bmi(body mass index )

# bmi=(weight_in_kg/height_in_meter square)

weight_in_kg=60

height_in_cm=165

height_in_meter=height_in_cm/100

bmi=weight_in_kg/height_in_meter**2

print(f"bmi of a person with height{height_in_cm} weight{weight_in_kg}={bmi}") 
