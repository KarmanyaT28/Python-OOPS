# Remove Dictionary Items

'''

using the del keyword
using the pop() method
using the popitem() method
using the clear() method
using dictionary comprehension

'''



# Remove Dictionary Items Using del Keyword

# Example 1
# In the following example, we are creating a dictionary named numbers with integer keys and their corresponding string values. Then, delete the item with the key '20' using the del keyword


numbers = {10:"Ten", 20:"Twenty", 30:"Thirty"}
print("Numbers dictionary before delete operation:", numbers)

del numbers[20]
print("Numbers dictionary after delete operation:", numbers)


#Example 2
# The del keyword, when used with a dictionary object, removes the dictionary from memory


numbers = {10:"Ten", 20:"Twenty", 30: "Thirty"}
print("Numbers dictionary before delete operation:", numbers)
del numbers
# print("Numbers dictionary after delete operation:", numbers)



# Remove Dictionary Items Using pop() Method

numbers1 = {10:"Ten", 20:"Twenty", 30: "Thirty", 40:"Fourty"}

print("numbers1 dictionary before delete operation:", numbers1)
val = numbers1.pop(20)
print("numbers1 dictionary after delete operation:", numbers1)
print("Value popped pop: ", val)



# Remove Dictionary Items Using popitem() Method

numbers = {10:"Ten", 20:"Twenty", 30: "Thirty"}
print("numbers1 dictionary before delete operation:", numbers)
val = numbers.popitem()
print("numbers1 dictionary after delete operation:", numbers)
print("Value popped popitem: ", val)


# Remove Dictionary Items using clear() methoc


numbers2 = {
    10:"Ten", 20:"Twenty",30: "Thirty",40:"Fourty",50:"Fifty",60:"Sixty"
}

print("numbers2 dictionary before clear operation:", numbers2)
numbers2.clear()
print("numbers2 dictionary after clear operation:", numbers2)



# Remove Dictionary Items using dictionary comprehension

student_info = {
    "name": "Alice",
    "Age": 21,
    "major":"Computer Science",
    "School": "Pace University, NYC"
}


keys_to_remove = ["age","major"]

for key in keys_to_remove:
    student_info.pop(key,None)

print(student_info)