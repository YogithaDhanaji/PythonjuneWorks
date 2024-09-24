text="abccddbb"

word_count={}

for char in text:
    if char in word_count:
        print(char , "first recursive character")

        break
    else:
        word_count[char]=1