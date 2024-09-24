from json import load # reference

f=open("C:\\Users\\LENOVO\\Desktop\\PythonJuneWorks\\jsaonWork\\data.json")

products=load(f)

for p in products:

    print(p.get("title"))