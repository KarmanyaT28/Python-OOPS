# Sort Arrays

'''
Using sorting algorithm:
Using the sort() method from list
Using the built in sorted() function
'''

# Sort arrays using a sorting algorithm

# Implementing a bubble sort algorithm

import array as arr
a = arr.array('i',[10,5,15,4,6,20,9])

for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if(a[i] > a[j]):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print(a)

print("**************************************************")
# Sort Arrays using Sort() Method:

import array as arr

#creating array

orgnlArray = arr.array('i',[10,5,15,4,6,20,9])
print("Original Array:",orgnlArray)

#converting to a list
sortedList = orgnlArray.tolist()
#sorting a list
sortedList.sort()


#creating array from sorted list
sortedArray = arr.array('i',sortedList)
print("Sorted Array:",sortedArray)


print("**************************************************")


# Sort Arrays Using Sorted() Method
import array as arr

b = arr.array('i', [10, 5, 15, 4, 6, 20, 9])

# The sorted() function returns a NEW list (not an array.array)
b_sorted_list = sorted(b)

print(b_sorted_list)
# Output: [4, 5, 6, 9, 10, 15, 20]


