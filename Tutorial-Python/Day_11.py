# Strings in Python

name = "Karmanya" #String
friend = "Python"
anotherFriend = "Lovish"

print("Hello, " + name)
print("**************************")
apple = "He said, \"He wants to eat an apple\""

# Another Option

apple1 = "He said, 'He wants to eat an apple'"

# \"<value>\"

print(apple)
print(apple1)
print("**************************")
string1 = '''He said
i dont know what you are talking about
i dont know??
What is this'''

print(string1)
print("**************************")
# Indexing
# Name
# Indexing starting with 0,1,2,3,4,5,6,7
print(name[0])

# print(name[8])
print(name[7])
print("**************************")
lengthofname = len(name)

# Another Solution:
for character in name:
    print(character)
print("**************************")
# My solution:
for i in range (0,lengthofname):
    print(name[i])


