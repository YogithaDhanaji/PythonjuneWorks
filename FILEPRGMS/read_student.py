f=open("C:\\Users\\LENOVO\\Desktop\\PythonJuneWorks\\FILEPRGMS\\students.txt","r")

student=[]

for stud in f:
    student.append(stud.rstrip("\n"))


print(student)    

