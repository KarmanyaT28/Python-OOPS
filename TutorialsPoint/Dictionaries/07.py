# Modifying Dictionary Values


person = {'Name': 'John', 'Age': 25, 'City': 'New York'}
# person.pop('Age')

person['Age'] = 26
print(person)


# Updating Multiple Dictionary Values

person = {'Name': 'Alice', 'Age': 25, 'City': 'New York'}
person.update({'Age': 26, 'City': 'Los Angeles'})
print(person)


# Conditional Dictionary Modification


if person['Age'] >= 26:
    person['Age'] = 29
    # print(person)


# while person['Age'] >=26:
    # print("BAD CALL") Infinite Loop

print(person)




# Modify Dictionary by Adding New Key-Value Pairs



# Using Assignment Operator
#Initial Dictionary

person = {'Name': 'Alice', 'Age': 25, 'City': 'New York'}
person['City'] = 'New York City'
print(person)


# Example: Using the setdefault() Method

# Initial Dictionary
person = {'Name': 'Alice', 'Age': 25}
person.setdefault('City', 'New York City')

print(person)
# person['City'] = ('Delhi')
# print(person)


# Modify Dictionary by Removing Key-Value Pairs

'''

Example: Using the del Statement
You can use the del statement to remove a specific key-value pair from a dictionary. In this example, 
the del statement removes the key 'age' along with its associated value from the 'person' dictionary

'''


del person['Age']
print(person)


# Using the pop() method

# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Removing the key-value pair associated with the key 'age'
removed_age = person.pop('age')

print(person)
print("Removed age:", removed_age)



'''

Example: Using the popitem() Method
You can use the popitem() method as well to remove the last key-value pair 
from a dictionary and return it as a tuple.

'''

person = {'name':'Alice', 'Age':25, 'City': 'New York'}
removed_item = person.popitem()


print(person)
print("Removed item:", removed_item)


