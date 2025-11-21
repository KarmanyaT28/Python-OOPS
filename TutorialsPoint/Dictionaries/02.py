# Only a number, string or tuple can be used as key
# All of them are immutable
d1 = {"Fruit":["Mango","Banana"], "Flower":["Rose","Lotus"]}

d2 = {('India','USA'):'Countries',('New Delhi','New York'):'Capitals'}

print(d1)
print(d2)


# Python doesn't accept mutable objects such as list as key, and raises TypeError.
#
# d1 = {["Mango","Banana"]:"Fruit","Flower":["Rose","Lotus"]}
# print(d1)


