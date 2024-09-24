
lst=[10,20,10,20,11,12,11,12,13,14]

# number_dict={}
# for num in number_dict:
#     if num in number_dict:

#         number_dict[num]+=1

#     else:
#         number_dict[num]=1  

# print(number_dict)          


# print(lst.count())

number_count={num:lst.count(num) for num in lst}

print(number_count)

text="hello hai hello hai hello"

word=text.split(" ")

word_count={w:word.count(w)for w in word}

print(word_count)