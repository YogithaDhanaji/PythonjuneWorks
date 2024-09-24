# dict={key:value}
# key should be uniqe

student={"name":"yogitha","course":"fullstack","core":"database"}
# print(type(student))

# print(student["course"])
# print(student.keys()) # print the keys in set

# student["name"]="hari" # update the key
# print(student["name"])

# student["place"]="kothamangalam" # overwrite the value if the key is presntt else add as a new pair
# print(student)


# new=student.items()
# print(new)

student={"name":"yogitha","course":"fullstack","core":"database","place":"kochi"}

# for i in student:
#     print(f"{i} = {student[i]}")


# update the course as data science in student in ineration

# for i in student:
#     student["course"]="data scince"

#     print(f"{i} = {student[i]}")

# delect the key if it perent in the dict using intration

for i in student.keys():
    print(i)
    if i =="place":
        new=student.pop(i)
print(new)
