# longest palindromic substring from given string

txt="racecar"

longest_palindrome=""

for i in range (0,len(txt)):

    left=i

    right=i


    while (left>=0 and right<len(txt)and txt[left]==txt[right]):

        current_palindrome=txt[left:right+1]

        if len(current_palindrome)>len(longest_palindrome):
            longest_palindrome=current_palindrome

        print(current_palindrome) 
        
        left=left-1

        right=right+1


print(longest_palindrome)

x='print(45)'

eval(x)


