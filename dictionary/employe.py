employee={"name":"yogi","dept":"pv","salary":50000,"combo_offer":1000}

# print all key value

for k,v in employee.items():
    print(k,v)


# check extra_working days oersent

# if ("extra_working_days"in employee):
#     print("present")

# else:
#     print("non present") 

employee["extra_working_day"]=3

# print(employee.get("extra_working_days"))

# print netpay

if "extra_working_day" in employee:

    netpay=employee.get("salary")+employee.get("combo_offer")*employee.get("extra_working_day")
    print(netpay)
else:
    netpay=employee.get("salary")
    print(netpay)



# fetching value from dictionaryusing key dict.get(key)
# adding new key value pair dict[key]=value    

  


