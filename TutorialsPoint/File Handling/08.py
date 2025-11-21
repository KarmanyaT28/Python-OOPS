# Directories in Python


# Checking if a directory Exists


import os

directory_path = "/Users/karmanya/PycharmProjects/Python-OOPS/TutorialsPoint/File Handling/MyFolder"

if os.path.exists(directory_path):
    print(f"The directory '{directory_path}' already exists!")

else:
    print(f"The directory '{directory_path}' does not exist!")



# In the following example, we are creating a new directory using the os.makedirs() function

import os

new_directory = "new_dir.txt"

try:
    os.makedirs(new_directory)
    print(f"Directory '{new_directory}' created successfully!")

except OSError as e:
    print(f"Error: Failed to create directory '{new_directory}': {e}")




# the mkdir() method


import os

os.mkdir("test")
print("Directory created successfully!")



# os.getcwd()


import os

current_directory = os.getcwd()
print(f"Current working directory is : {current_directory}")




# Listing Files and Directories

import os
directory_path = r"/Users/karmanya/PycharmProjects/Python-OOPS/TutorialsPoint/File Handling"


try:
    contents = os.listdir(directory_path)
    print(f"Contents of '{directory_path}' are : ")
    for item in contents:
        print(item)

except OSError as e:
    print(f"Error: Failed to find '{directory_path}': {e}")



# os.chdir("newdir")


import os
new_directory = r"/Users/karmanya/PycharmProjects/Python-OOPS/TutorialsPoint/File Handling"

try:
    os.chdir(new_directory)
    print(f"Current working directory is : {new_directory}")

except OSError as e:
    print(f"Error: Failed to find '{new_directory}': {e}")




# removing a directory

import os
directory_path = r"/Users/karmanya/PycharmProjects/Python-OOPS/TutorialsPoint/File Handling/new_dir"


try:
    os.rmdir(directory_path)
    print(f"Directory '{directory_path}' was successfully removed!")

except OSError as e:
    print(f"Error: Failed to remove '{directory_path}': {e}")