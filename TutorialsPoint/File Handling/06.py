'''

In the example below, we are opening the
file "example.txt" in read mode.
We then use the readline() method to read
the first line of the file

'''

# Open the file in read mode

file = open('example.txt','r')

# Read the first line of the file

line= file.readline()

print(line)

file.close()



'''

In this example, we are opening the file "example.txt" in read mode.
We then use the readlines() method to read all the lines from the file 
and return them as a list of strings

'''

# Open the file in read mode
file = open('example.txt', 'r')

# Read all lines from the file
lines = file.readlines()

# Print the lines
for line in lines:
    print(line, end='')


file.close()




'''

The "with" statement in Python is used for exception handling. When dealing with files, using the "with" statement ensures that the file is properly closed after reading, even if an exception occurs.

When you use a with statement to open a file, the file is automatically closed at the end of the block, even if an error occurs within the block.



'''


with open("example.txt","r") as file:
    content = file.read()
    print(content)

'''Reading a File in Binary Mode
By default, read/write operation on a file object are performed on text string data. If we want to handle files of different types, such as media files (mp3), executables (exe), or pictures (jpg), we must open the file in binary mode by adding the 'b' prefix to the read/write mode.

Writing to a Binary File
'''


with open("test.bin",'wb') as file:
    data = b"Hello, World!"
    file.write(data)



'''
To read a binary file, we need to open it in 'rb' mode. The returned value of the read() method is then decoded before printing

'''

with open("test.bin","rb") as file:
    data = file.read()
    print(data.decode(encoding="utf-8"))



'''

Reading Integer Data From a File
To write integer data to a binary file, the integer object should be converted to bytes using the to_bytes() method.

Writing an Integer to a Binary File
Following is an example on how to write an integer to a binary file

'''



n=25
data = n.to_bytes(8,'big')

with open("test.bin","wb") as file:
    file.write(data)


# Writing a float to a binary file


import struct

x = 23.50

# Pack the float into a binary format
data = struct.pack('f',x)
with open("test.bin","wb") as file:
    file.write(data)


# Reading the float numbers from a binary file

with open("test.bin","rb") as file:
    data = file.read()

    x = struct.unpack('f',data)[0]


    print(x)



'''

The following program opens a file in 'r+' mode (read-write mode), 
seeks a certain position in the 
file, and reads data from that position

'''


with open("foo.txt", "r+") as fo:
    fo.seek(10,0)


    data = fo.read(3)

    print(data)


'''

In this example, we open the file in 'r+' mode and write data to the file. 
The seek(0) method repositions the pointer to the beginning of the file

'''


with open("foo.txt", "r+") as fo:
    fo.write("This is a rat race")


    fo.seek(0)


    data = fo.read()

    print(data)


'''

The following example demonstrates how to use the seek() method to perform 
simultaneous read/write operations on a file. 
The file is opened in w+ mode (read-write mode), some data is added, 
and then the file is read and modified at a specific position

'''


# Open a file in read-write mode
fo = open("foo.txt", "w+")

# Write initial data to the file
fo.write("This is a rat race")

# Seek to a specific position in the file
fo.seek(10, 0)

# Read a few bytes from the current position
data = fo.read(3)
print("Data read from position 10:", data)

# Seek back to the same position
fo.seek(10, 0)

# Overwrite the earlier contents with new text
fo.write("cat")

# Rewind to the beginning of the file
fo.seek(0, 0)

# Read the entire file content
data = fo.read()
print("Updated file content:", data)

# Close the file
fo.close()