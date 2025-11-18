# Lists in python

l = [3,5,6]
print(l)
print(type(l))

marks = [3,5,6,5,32,4,5,3,2,6]
print(marks)
print(type(marks))

print(marks[0])
print(marks[1])
print(marks[2])

print(marks[-3])

print(marks[len(marks)-3])
print(marks[5-3])
print(marks[2])


if 6 in marks:
    print("Yes")
else:
    print("No")


print(marks)

print(marks[1:8])

print(marks[1:8:2])



lst = [i*i for i in range(10)]
print(lst)

lst1 = [i*i for i in range(10) if i%2==0]
print(lst1)


l = [1,2,4,6,6,5,4,3,2,1,1,1,1,1,88]
print(l)

l.append(7)
print(l)

l.sort(reverse=True)
l.sort(reverse=False)
print(l)


l.reverse()
print(l)


print(l.index(1))


print(l.count(1))


m = l.copy()
m[0] = 0
print(m)

l.insert(1,899)

print(l)


m = [900,1000,1100,1200,1300,1400,1500,1600,1700,1800]
l.extend(m)
print(l)

k = l+m
print(k)


