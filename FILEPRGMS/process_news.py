f=open("C:\\Users\\LENOVO\\Desktop\\PythonJuneWorks\\FILEPRGMS\\news.txt","r")
# word_list=[]
# for line in f:
#     word=line.rstrip("\n")

#     words=word.split(" ")

#     for w in words:

#         word_list.append(w)

# print(word_list)


word_list=[ w for line in f for w in line.rstrip("\n").split(" ")]
print(word_list)

wc={w:word_list.count(w) for w in word_list}

print(wc)