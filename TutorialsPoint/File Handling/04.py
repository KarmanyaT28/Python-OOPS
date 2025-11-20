# Python - Write to a file


# Using write() method

with open("example.txt", "w") as file:
    file.write("Hello")
    file.write("World, THis is a new line")
print("File Opened Successfully")


# Using writelines() method

lines = ["First line\n",
         "Second line\n","Third line\n","Fourth line\n"]

with open("example.txt", "w") as file:
    file.writelines(lines)

print("File Opened Successfully")


# Writing to a New File
# Open the File − Use the open() function to create or open a file in write mode ("w" or "wb" for binary files).
#
# Write Data − Use the write() or writelines() method to write data to the file.
#
# Close the File − Ensure the file is properly closed after writing, generally using the "with" statement for automatic handling.
#


# Example

fo = open("foo.txt","w")
fo.write("Python is a great language.\n Yeah it is great!!\n")


fo.close()

with open("foo.txt","r") as file:
    content = file.read()
    print(content)



# Writing to a New File in Binary Mode


with open('test.bin', 'wb') as file:
    # Binary Data
    data = b"Hello, World!"
    file.write(data)