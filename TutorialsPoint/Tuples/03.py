# Accessing range of tuple items with negative indexing


tup1 = ("a", "b", "c", "d")
tup2 = (1, 2, 3, 4, 5)

print ("Items from index 1 to last in tup1: ", tup1[1:])
print ("Items from index 2 to last in tup2", tup2[2:-1])




tuple1 = ("a", "b", "c", "d")
tuple2 = (25.50, True, -55, 1+2j)
tuple3 = (1, 2, 3, 4, 5)
tuple4 = ("Rohan", "Physics", 21, 69.75)

print ("Items from index 1 to last in tuple1: ", tuple1[1:])
print ("Items from index 0 to 1 in tuple2: ", tuple2[:2])
print ("Items from index 0 to index last in tuple3", tuple3[:])



tuple1 = ("a", "b", "c", "d")
tuple2 = (25.50, True, -55, 1+2j)

print ("Items from index 1 to 2 in tuple1: ", tuple1[1:3])
print ("Items from index 0 to 1 in tuple2: ", tuple2[0:2])