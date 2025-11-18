# Loop through set items

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




