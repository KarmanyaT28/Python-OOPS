# Loop through tuple items with index

tup = (25,12,10,-21,10,100)

indices = range(len(tup))
for i in indices:
    print("tup[{}]: ".format(i), tup[i])

