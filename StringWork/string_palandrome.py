# create a function is_palindrome (word)return true if word is a palindromic string
# else return false

word=str(input("enter word"))


is_palindrome=True

reversed_str=word[::-1]

if word==reversed_str:
    print(is_palindrome)


else:
    print(False)    


# logic2

def is_palindrome(word):

    reversed_str=word[::-1]

    return word==reversed_str

print(is_palindrome("madam"))

# creat a function reversed(word) return revesed_string

def reversed(word):

    reversed_str=word[::-1]

    return reversed_str

print(reversed("hello"))
