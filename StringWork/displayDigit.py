word= 'i have 2 bike and 1 car'

# print alphebets

for ch in word:

    if ch.isalpha():

        print(ch, end=(" "))

# print digits

for ch in word:

    if ch.isdigit():

        print(ch, end=(" "))        

for ch in word:

    if ch.isalnum():

        print(ch,end=(" "))        
