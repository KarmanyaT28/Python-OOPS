# For Loop with else in python



# for i in [0,1,2,3,4,5]:
for i in range(5):
    print(i)

else:
    print("Sorry , No i")



for i in range(6):
    print(i)
    if i == 4:
        break

else: #Loop has finished successfully not 'break'
    print("Sorry , No i")


# Similarly with while loop


i = 0
while i<7:
    print(i)
    i = i + 1
    if i==5:
        break


else:
    print("Loop has finished execution perfectly ")


