mobiles=[

    {"id":100,"title":"s23 ultra","brand":"samsung","price":125000,"network":"5g"},
    {"id":101,"title":"s23","brand":"samsung","price":54000,"network":"4g"},
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},
    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},
]

# print all mobile_name

# print all brand

# mobile_name=[n.get("title") for n in mobiles]

# print(mobile_name)

# brands=[b.get("brand") for b in mobiles]

# print(set(brands))

# print sumsang mobils

# sumsang_mobiles=[mob.get("title") for mob in mobiles if mob.get("brand")==("samsung") ]

# print(sumsang_mobiles)

#print all mobiles in range of 23k to 40k

# range_mobiles=[mob.get("title") for mob in mobiles if mob.get("price")>=23000 and mob.get("price")<=40000]


# print(range_mobiles)

# or 

# range_mobiles=[mob.get("title")for mob in mobiles if mob.get("price") in range (23000,40001)]
# print(range_mobiles)

# max_price=0

# for mob in mobiles:
#     if mob.get ("price")>max_price:
#         max_price=mob.get("price")

# costly_mobile=[mob.get("title") for mob in mobiles if mob.get("price")==max_price] 

# print(costly_mobile)

def get_price(mob):

    return mob.get("price")

costly_mobile=max(mobiles,key=get_price)

Cheapest_mobile=min(mobiles,key=get_price)

print(Cheapest_mobile)

sorted_mobiles=sorted(mobiles,key=get_price,reverse=True)

print(sorted_mobiles)