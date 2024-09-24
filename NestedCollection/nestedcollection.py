arr=[
    [10,20],
    [21,30],
    [40,53]
]
# numbers=[ num for lst in arr for num in lst]

# print(sum(numbers))

        
evens=[ num for lst in arr for num in lst if num%2==0]

print(evens)