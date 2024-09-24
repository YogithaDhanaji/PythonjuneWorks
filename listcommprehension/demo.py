list=[10,2,3,5,6,5]


# square=[return iteration condition]

square=[n**2 for n in list ]

cubes=[n**3 for n in list ]

print(square)

print(cubes)

even_numbers=[n for n in list if n%2==0]

odd_number=[n for n in list if n%2!=0]

print(odd_number)
print(even_numbers)

words=["fly","flyin","flyout","flyoff","out","in"]

# print list of words starting with fiy

fliter_word=[w for w in words if w.startswith("fly")]

print(fliter_word)