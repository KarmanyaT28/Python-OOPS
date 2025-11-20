# Writing to a file in python

# Using the write() method

with open("foo.txt", "w") as file:
    file.write("Hello Python!")
    print("Contect added successfully")

with open("foo.txt", "r") as file:
    content = file.read()
    print(content)

# Using the writelines() method

lines = ["First line\n", "Second line\n", "Third line\n"]

with open("foo.txt", "w") as file:
    file.writelines(lines)
    print("Contect added successfully")

with open("foo.txt", "r") as file:
    content = file.read()
    print(content)



# Closing a file in python


file = open("example.txt", "w")
file.write("Hello Python!, This is an example line to close")
file.close()

print("File closed successfully")