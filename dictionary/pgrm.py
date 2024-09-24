# creat a dictionry moabile with keys name,brand,price,price,is_avilable

mobile={"name":"redmi 8a ","brand":"redmi","price":12000,"is_available":True,"offer":500}

# pprint mobile name

# print(mobile["name"])

# print(mobile.get("rice"))

# print(mobile["is_available"])

# all_keys=mobile.keys()
# print(all_keys)

# all_values=mobile.values()
# print(all_values)


# for k,v in mobile.items():

#     print(k,v)

# mobile.pop("name")
mobile["offer"]=1000
print(mobile)

# get(key) 
# valuve()
# keys()
# items()
# pop(keys)
#

if "offer" in mobile:
    selling_price=mobile.get("price")-mobile.get("offer")

    print(selling_price)

else:
    selling_price=mobile.get("price")

    print(selling_price)    