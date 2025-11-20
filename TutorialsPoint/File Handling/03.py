# Using "with" statement for automatic file closing


# Example

with open("example.txt", "w") as file:
    file.write("This is an example using the with statement")
    print("File closed successfully")


'''
In this example, the file is automatically closed at the end of the with block, so there is no need to call close() method explicitly
'''

# fo = open("example.txt","r")
#
# print(fo.closed)



# Handling exceptions when closing a file

try:
    file = open("example.txt","w")
    file.write("This is an example using the exception handling")

finally:

    file.close()
    print("File closed successfully")


'''
In Python, we use a try-finally block to handle exceptions when closing a file. The "finally" block ensures that the file is closed regardless of whether an error occurs in the try block


'''