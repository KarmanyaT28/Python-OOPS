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


# Converting Text Strings to Bytes

# Open a file in binary write mode

with open('test.bin', 'wb') as f:
    # Convert text string to bytes
    data = "Hello, World!".encode('utf-8')
    f.write(data)


# Writing to an Existing File
# Open a file in append mode
fo = open("foo.txt","a")
text = "Tutorials Point has python tutorial"

fo.write(text)

fo.close()



'''
The following program demonstrates how to open a file in 
read-write mode ('w+'), write some data, seek a specific 
position, and then overwrite part of the file's content 
'''



# open a file in read-write mode
fo = open("foo.txt","w+")

# write initial data to the file
fo.write("This is a rat race")

# Move the read/write pointer to the 10th byte
fo.seek(10,0)

# Read 3 bytes from the current position
data = fo.read(3)

# Move the read/write pointer back to the 10th byte
fo.seek(10,0)

# Overwrite the existing content with new text
fo.write('cat')

# Close the file
fo.close()

