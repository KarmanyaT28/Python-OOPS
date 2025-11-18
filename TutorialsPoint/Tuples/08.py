# Joining Tuples in Python

# Joining Tuples Using Concatenation ("+") Operator


# Two tuples to be joined

T1 = (10,20,30,40)
T2 = ('one','two','three','four')

# Joining the tuples

joined_tuple = T1 + T2


print("Joined tuple: ", joined_tuple)
print("\n")



# Joining Tuples Using List Comprehension

T1 = (36,24,3)
T2 = (84,5,81)

joined_tuple = [item for subtuple in [T1,T2] for item in subtuple]

print("Joined tuple: ", joined_tuple)
print("\n")




# Joining Tuples Using extend() Function


T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
L1 = list(T1)
L2 = list(T2)
L1.extend(L2)
T1 = tuple(L1)
print ("Joined Tuple:", T1)



# Join Tuples using sum() Function

T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
T3 = sum((T1, T2), ())
print ("Joined Tuple:", T3)



# Joining Tuples using for Loop

T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
for t in T2:
   T1+=(t,)
print (T1)
