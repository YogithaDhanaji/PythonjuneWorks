# courses=("python",)

# print(type(courses))


num=[1,2,[3,(100,200,300),4],5,6]

new=num[2]

ele_four=new.pop()

new.insert(1,ele_four)
print(new)

new1=num[2][2]
l=list(new1)
l.insert(1,150)
l1=tuple(l)

num[2][2]=l1
print(num)

