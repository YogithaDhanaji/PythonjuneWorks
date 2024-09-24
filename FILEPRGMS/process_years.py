f_read=open("C:\\Users\\LENOVO\\Desktop\\PythonJuneWorks\\FILEPRGMS\\years.txt","r")
f_century=open("C:\\Users\\LENOVO\\Desktop\\PythonJuneWorks\\FILEPRGMS\\century.txt","w")
f_non_century=open("C:\\Users\\LENOVO\\Desktop\\PythonJuneWorks\\FILEPRGMS\\non_century.txt","w")


for year in f_read:

    y=int(year.rstrip("\n"))

    if y%100==0:

        f_century.write(str(y)+"\n")


    else:
        f_non_century.write(str(y)+"\n")    