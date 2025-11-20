# Loop through set items
from _ast import comprehension

my_set = {25,12,10,-21,10,100}

for item in my_set:
    print("Item: ",item)

print("********************")
my_set1 = {25,12,10,-21,10,100}
set_iterator = iter(my_set1)

while True:
   try:
      # Getting the next item from the iterator
      item = next(set_iterator)
      # Performing operations on each element
      print("Item:", item)
   except StopIteration:
      # If StopIteration is raised, break from the loop
      break



# Iterable using set comprehension

numbers = [1,2,3,4,5]

squares_of_evens = {x**2 for x in numbers if x % 2 == 0}
print(squares_of_evens)



# Iterable through a set using the enumerate function


my_set2 = {2,3,4,5,6}
set_list = list(my_set2)

for index, item in enumerate(set_list):
    print("Index: ",index, "Item: ", item)




# Loop Through Set Items with add() Method


my_set3 = set()


for i in range(5):
    my_set3.add(i)

print(my_set3)