# Python - Renaming and Deleting Files


import os

current_name = "oldfile.txt"

new_name = "newfile.txt"


os.rename(current_name, new_name)

print(f"File '{current_name}' renamed to '{new_name}' successfully")





# deleting the files


import os

file_to_delete = "file_to_delete.txt.py"

os.remove(file_to_delete)

print(f"File '{file_to_delete}' deleted successfully")