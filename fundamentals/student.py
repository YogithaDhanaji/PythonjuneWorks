# write a progarm to read student name and 3 marks mark1,mark2,mark3
# and print totalmark and average mark

student_name=input("enter studen Name")

mark1=input("enter mark1")

mark2=input("enter mar2")

mark3=input("enter mark3")

total_mark=int(mark1)+int(mark2)+int(mark3)

average_mark=total_mark/3

print(f"studen_name:{student_name}, total mark: {total_mark} and average mark: {average_mark}")
