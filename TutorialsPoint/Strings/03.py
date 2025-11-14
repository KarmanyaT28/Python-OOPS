var = "HELLO PYTHON"

print(var[0])
print(var[7])
print(var[11])
# print(var[12]) string index out of range


var = "HELLO PYTHON"
print(var[-1])
print(var[-5])
print(var[-12])



var1 = "HRLLO PYTHON"
# var1[1] = "E"
# print(var1) #'str' object does not support item assignment



print("var1:",var1)
print("var[3:8]:", var1[3:8])


print("var1[-9:-4]:", var1[-9:-4])


print("var1[0:5]:", var1[0:5])
print("var1[:5]:", var1[:5])

print("var1:",var1)


print("var1[6:12]:", var[6:12])

print("var1[6:]:", var1[6:])

print("var1[:]:", var1[:])


# var="HELLO PYTHON"
# print ("var:",var)
print(len(var1))
print ("var1[-1:7]:", var1[len(var1)-1:7])
print ("var1[7:0]:", var1[7:0])




print ("var1:",var1)
print ("var1[:6][:2]:", var1[:6][:2])

var2=var1[:6]
print ("slice:", var2)
print ("var2[:2]:", var2[:2])