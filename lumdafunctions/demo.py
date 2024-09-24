# def add(n1,n2):
#     return n1+n2

# print(add(10,20))




add=lambda n1,n2:n1+n2
print(add(100,200))


sub=lambda n1,n2,n3:n1-n2-n3
print(sub(10,2,3))

cube=lambda n:n**3
print(cube(2))

max_two=lambda n1,n2:n1 if n1>n2 else n2

print(max_two(10,5))

min_two=lambda n1,n2 :n1 if n1<n2 else n2

print(min_two(20,30))

last_digit_max=lambda n1,n2:n1 if n1%10>n2%10 else n2

print(last_digit_max(121,343))

odd_even=lambda n1: "odd" if n1%2!=0 else "even"

print(odd_even(3))