# Tuple Methods


print(dir((1, 2)))
print(help((1, 2).index))


tup1 = (25,12,10,-21,10,100)
print("Tup1:", tup1)
x = tup1.index(10)
print("First index of 10: ", x)

tup2 = (10,20,30,40,50,60)
print("Tup2:", tup2)

c = tup2.count(10)
print("Count of 10: ", c)


# Even if the items in the tuple contain expressions, they will be evaluated to obtain the count.


tup1 = (10, 20/80, 0.25, 10/40, 30, 10, 55)
print ("Tup1:", tup1)
c = tup1.count(0.25)
print ("count of 0.25:", c)