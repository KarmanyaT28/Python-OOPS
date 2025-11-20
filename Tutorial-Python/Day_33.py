dicti = {
    "Karmanya": "Human Being",
    "Spoon": "Object"
}

print(dicti["Karmanya"])

print(dict["Karmanya"])




dic1 = {
    344: "Karmanya",
    56: "Shubham",
    678: "Zakir",
    567: "Neha"
}


print(dic1[567])


info = {'Karmanya': "Human Being","Spoon": "Object", 'Eligible':True}
print(info)

info1 = {'name':'Karan','age':25, 'Eligible':True}
print(info1)

print(info1['name'])
print(info1.get('Eligible'))


print(info1.keys())

print(info1.values())


for key in info.keys():
    print(key)
    print(info[key])
    print("XXXXXXXXXXXXXXXXXX")




for key in info1.keys():
    print(f"The value corresponding to the key {key} is: {info1[key]}")



# Accessing Keys
print(info.items())


for key,value in info.items():
    print(f"The value corresponding to the key {key} is: {value}")


