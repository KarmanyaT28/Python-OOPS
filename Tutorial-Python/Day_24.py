# Operations on tuple

countries = ("Spain", "USA", "Italy", "India", "England")

# Convert to list
temp = list(countries)
temp.append("Canada")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)




countries = ("Spain", "USA", "Italy", "India", "England")
countries1 = ("Vietnam","India","China")

print(countries)
print(countries1)

totalcountries = countries + countries1
print(totalcountries)




tuple1= (0,1,2,3,2,3,1,3,2,3)

res = tuple1.count(3)

print("The count of 3 in tuple1 is : ", res)



res = tuple1.index(3,4,8)
print("The index of 3 in tuple1 is : ", res)




