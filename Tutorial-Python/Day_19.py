# break and continue in python

for i in range(12):
    print("5 X", i+1, "=", 5 * (i+1) )
    if(i==9):
        break

print("Left the loop")

print("*********************************")

for j in range(12):
    if(j == 11):
        print("Skip the iteration")
        continue

    print("5 X", j, "=", 5 * j )




# do while loop

# emulate

while True:
    print(i)
    i = i+1
    if(i%100 == 0):
        break