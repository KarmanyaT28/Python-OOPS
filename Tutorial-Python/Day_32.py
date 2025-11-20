# Set Methods in python

s1 = {1,2,3,5,6}
s2 = {3,6,7}

# print(s1.union(s2))

s1.update(s2)

# print(s1,s2)


cities = {"Tokyo", "Madrid", "Toronto", "Mumbai", "New York"}
# print(cities)

cities2 = {"New York", "Toronto", "Mumbai"}


cities3 = cities.union(cities2)
# print(cities3)


cities4 = cities.intersection(cities2)
# print(cities4)





cities.intersection_update(cities2)
# print(cities)


cities5 = cities.symmetric_difference(cities2)
# print(cities5)



citiesk = {"Tokyo","Madrid","Berlin","Delhi"}
citiesn = {"Seoul","Kabul","Delhi"}

cities6 = citiesk.difference(citiesn)
cities7 = citiesk.symmetric_difference(citiesn)
print(cities6)
print(cities7)



cities = {"Tokyo", "Madrid", "Toronto", "Mumbai", "New York"}
# print(cities)

cities2 = {"New York", "Toronto", "Mumbai"}

print(cities.issuperset(cities2))
print(cities2.issuperset(cities))
print(citiesk.issuperset(citiesn))
print(citiesn.issuperset(citiesk))

print(cities2.issubset(cities))



cities = {"Tokyo", "Madrid", "Toronto", "Mumbai", "New York", "tokyo23"}

cities.add("Muzaffarnagar")
print(cities)


cities.remove("Madrid")
print(cities)


cities.discard("tokyo23")
print(cities)


cities = {"Tokyo", "Madrid", "Toronto", "Mumbai", "Madras", "Kolkata"}
item = cities.pop()
print(cities)
print(item)


del cities
# print(cities)

'''
New York
Boston
Washington
Philadelphia
New Jersey
California
'''


info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present")
else:
    print("Carla is not present")