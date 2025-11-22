# Add Dictionary Items

# Adding Dictionary Items in Python refers to inserting new key-value pairs into an existing dictionary


'''

Using square brackets
Using the update() method
Using a comprehension
Using unpacking
Using the Union Operator
Using the |= Operator
Using setdefault() method
Using collections.defaultdict() method


'''


# Add Dictionary Item using Square Brackets

marks = {"Savita":67,"Imtiaz":88,"Laxman":91,"David":33}
print("Initial Dictionary",marks)

marks['Kavya'] = 58
print("Dictionary after new addition: ", marks)


# Add Dictionary Item Using the update() Method


marks.update({'Kavya': 65, 'Mohan': 98})
print("Dictionary after update: ", marks)


# Add Dictionary Item using Unpacking

marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
newmarks = {**marks, **marks1}
print ("marks dictionary after update: \n", newmarks)


# Add Dictionary Item Using the Union Operator (|)


marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":33}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
newmarks = marks | marks1

print ("marks dictionary after update: \n", newmarks)


# Add Dictionary Item Using the "|=" Operator


marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
marks |= marks1
print ("marks dictionary after update marks: \n", marks)


# Add Dictionary Item Using the setdefault() Method


# Initial Dictionary
student = {"name": "Alice", "Age": 21}

major = student.setdefault("major", "Computer Science")
print(student)