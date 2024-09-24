
word1="PQRStvwxyz"

word2="ABCDEFG"

smalllest_word=word1 if len(word1)< len(word2) else word2

merged_word=""

for i in range(0,len(smalllest_word)):

    merged_word=merged_word+word1[i]+word2[i]

if len(word1) >len (word2):

    balance=word1[len(smalllest_word):]


else:
    balance=word2[len(smalllest_word):]


merged_word=merged_word+balance

print(merged_word)
