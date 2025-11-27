list1 = [1,2,3]
list2 = ["Rohan","Karmanya","Hello",1,2,3.5]
list3 = [25.50, True, -55, 1+2j]
list4 = ["a","b","c","d"]

print(list1)
print(list2)
print(list3)
print(list4)


# Accessing Values in Lists

list1 = [1,2,3,'python','mern',1997,2000]
list2 = [1,2,3,4,5,6,7]
print(list1[4])
print(list2[2])
print ("list2[1:5]: ", list2[1:5])


# Updating lists

list = ["Update","The","List"]
print(list)

list[1]="This"
print(list)



# Delete List Elements
list5 = [1,2,3,4,5,6,7]
print(list5)

del list5[0]
print(list5)




'''



Python List Operations
In Python, List is a sequence. Hence, we can concatenate two lists with "+" operator and concatenate multiple copies of a list with "*" operator. The membership operators "in" and "not in" work with list object.

Python Expression	Results	Description
[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	Concatenation
['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	Repetition
3 in [1, 2, 3]	True	Membership
Indexing, Slicing, and Matrixes
Because lists are sequences, indexing and slicing work the same way for lists as they do for strings.

Assuming following input −

L = ['spam', 'Spam', 'SPAM!']
Python Expression	Results	Description
L[2]	SPAM!	Offsets start at zero
L[-2]	Spam	Negative: count from the right
L[1:]	['Spam', 'SPAM!']	Slicing fetches sections
Python List Methods
Python includes following list methods −

Sr.No.	Methods with Description
1	
list.append(obj)

Appends object obj to list.

2	
list.clear()

Clears the contents of list.

3	
list.copy()

Returns a copy of the list object.

4	
list.count(obj)

Returns count of how many times obj occurs in list

5	
list.extend(seq)

Appends the contents of seq to list

6	
list.index(obj)

Returns the lowest index in list that obj appears

7	
list.insert(index, obj)

Inserts object obj into list at offset index

8	
list.pop(obj=list[-1])

Removes and returns last object or obj from list

9	
list.remove(obj)

Removes object obj from list

10	
list.reverse()

Reverses objects of list in place

11	
list.sort([func])

Sorts objects of list, use compare func if given

Built-in Functions with Lists
Following are the built-in functions we can use with lists −

Sr.No.	Function with Description
1	cmp(list1, list2)
Compares elements of both lists.

2	len(list)
Gives the total length of the list.

3	max(list)
Returns item from the list with max value.

4	min(list)
Returns item from the list with min value.

5	list(seq)
Converts a tuple into list.





'''