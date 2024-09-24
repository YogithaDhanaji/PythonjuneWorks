text='the quick brown fox jumps over a lazy dog'

alphabets="abcdefghijklmnopqrstuvwxyz"

text=text.casefold()

is_panagram=True

for ch in text:

    if text.count(ch)==0:

        is_panagram=False

        break

print(is_panagram)


