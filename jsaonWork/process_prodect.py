from json import load


f=open("C:\\Users\\LENOVO\\Desktop\\PythonJuneWorks\\jsaonWork\\products.json",encoding="UTF-8")

items=load(f)

print(len(items))


# for p in items:

#     print(p.get("title"))


item=[i.get("title") for i in items]

# print(item)


jew_prodect=[i.get ("title")for i in items if i.get("category")=="jewelery"]

# print(jew_prodect)

price_filter=[i.get("title") for i in items if i.get("price")>=100 and i.get("price")<=150]

# print(price_filter)


#prodect with most no of rating

def get_rating_count(dic):

    return dic.get("rating").get("count")

top_selling_max=max(items,key=get_rating_count)

print(top_selling_max)