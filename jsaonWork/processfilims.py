from json import load

f=open("C:\\Users\\LENOVO\\Desktop\\PythonJuneWorks\\jsaonWork\\filim.json")

movies=load(f)

for m in movies:

    print(m.get("title"))
