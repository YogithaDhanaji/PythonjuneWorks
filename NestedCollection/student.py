student=[
    {"id":100,"name":"yogi","course":"test","mark":450},
    {"id":101,"name":"amal","course":"mern","mark":470},
    {"id":102,"name":"alex","course":"django","mark":420},
    {"id":103,"name":"ashin","course":"data","mark":480},
    {"id":104,"name":"joy","course":"django","mark":400},
    {"id":105,"name":"nam","course":"sql","mark":410},
    {"id":106,"name":"allf","course":"django","mark":490},
    {"id":107,"name":"doo","course":"django","mark":420},

]

# print all student names
# student_name=[ st.get("name") for st in student]

# print(student_name)

# all_course=[st.get("course") for st in student]

# print(set(all_course))


# django_stud=[ st.get("name")for st in student if st.get("course")=="django"]

# print(django_stud)

# mark_filter=[st.get("name")for st in student if st.get("mark")>=450 and st.get("mark")<=480 ]

# print(mark_filter)


max_mark=0

for st in student:
    if st.get("mark")>max_mark:
        max_mark=st.get("mark")

max_mark_student=[st.get("name") for st in student if st.get("mark")==max_mark]

print(max_mark_student)        


def get_mark(stud):
    return stud.get ("mark")

top_student=max(student,key=get_mark)

print(top_student)



sorted_students=sorted(student,key=get_mark)
print(sorted_students)