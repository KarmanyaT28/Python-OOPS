# for loop in arrays


import array as arr

newArray = arr.array('i',[56,42,23,85,45])

for item in newArray:
    print(item)

print("******************************")
# while loop in arrays

a = arr.array('i',[56,42,23,85,45,394,398493,2,34,54,24])

length_Array = len(a)


idx = 0


while idx<length_Array:
    print(a[idx])
    idx+=1



print("******************************")


# python for loop with array index

b= arr.array('d',[56,42,23,34,456])

length_Array1 = len(b)
for x in range(length_Array1):
    print(a[x])