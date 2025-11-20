'''r - Opens a file for reading only

rb - Opens a file for reading only in binary format

r+ - Opens a file for reading and writing

rb+ - Opens a file for reading and writing in binary format

w - Opens a file for writing

b - Opens a file in binary mode

t - Opens a file in text mode

+ - Opens a file for updating(Reading and Writing)

wb - Opens a file for writing in binary format

w+ - Opens a file for writing and reading

wb+ - Opens a file for reading writing in binary

a - opens a file for appending

ab - opens a file for appending in binary

a+ -  opens a file for both appending and reading

ab+ - opens a file for both appending and reading in binary mode

x - open for exclusive creation, failing if the file already exists


'''


# Example - 1

# # Opening a file in read mode
# file = open("example.txt", "r")
#
# # Opening a file in write mode
# file = open("example.txt", "w")
#
# # Opening a file in append mode
# file = open("example.txt", "a")
#
# # Opening a file in binary read mode
# file = open("example.txt", "rb")
#

# Example-2


fo = open("foo.txt","wb")

print("Name of the file:", fo.name)
print("Closed or not: ", fo.closed)
print("Opening mode: ", fo.mode)


fo.close()
print("Closed or not: ", fo.closed)


# Reading a file in python

#
# read() - Reads the entire file
# readline() - Reads one line at a time
# readlines() - Reads all lines into a list
#

print("\n")
print("**************Method-1**************")
print("\n")
# Using read() method

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
print("\n")
print("**************Method-2**************")
print("\n")
# Using readline() method

with open("example.txt", "r") as file:
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()


# Using readlines() method
print("\n")
print("**************Method-3**************")
print("\n")
with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')

