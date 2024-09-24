placment={"testing":45,"python":39,"bigdata":32,"asp":56,"java":60}

def get_value(key):
    return placment.get(key)


srt=sorted(placment,key=get_value,reverse=True)

print(srt)