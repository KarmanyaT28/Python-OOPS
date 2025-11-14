# # Quick Quiz
#
# nm = "Karmanya"
# print(nm[-4:-2])


# String Methods


a = "Karmanya"

print(len(a))


# Concept of immutability - Strings are immutable
# This will not change string a , it will create a new string
print(a)
print(a.upper())
print(a.lower())


a1 = "String2333333333333"

print(a1.rstrip("3"))


string1 = "Karmanya is a very bad boy"
print(string1)
print(string1.replace("Karmanya","John"))



a2 = "Karmanya is a coder"

print(a2)
print(a2.split(" ")) # Converts into lists for words separated by a space


blogHeading = "introduction to js"

print(blogHeading.capitalize()) # Capitalizes the first character of first word


blogheading1 = "introduction to PyThOn"

print(blogheading1.capitalize()) # Also arranges every character to lowercase

str1 = "Welcome to the console!"
print(str1.center(50))


print(len(str1))
print(len(str1.center(50)))

a = "Karmanya Karmanya is studying"

print(a.count("Karmanya"))


str3 = "Welcome to the Console !!!"
print(str3.endswith("!!!"))


str4 = "Welcome to the Console !!!"
print(str4.endswith("to",4,10))



str5 = "Name is Dan. He is an honest man"
print(str5.find("is"))


print(str5.find("ishhh"))
# print(str5.index("ishhh"))


str6 = "Welcometotheconsole"
print(str6.isalnum())


str7 = "NewString007"
print(str7.isalpha())
print(str7.isalnum())


str8 = "hello world"
print(str8.islower())


str9 = "We wish you all the best\n"
str10 = "We wish you all the best"
print(str9)
print(str9.isprintable())
print(str10.isprintable())



str11 = "              "
print(str11.isspace())



str12 = "World Health Organization"
print(str12)
print(str12.istitle())

str13 = "To kill a Mocking bird"
print(str13.istitle())


str14 = "Python is an interpreted language"
print(str14.startswith("Python"))


str15 = "python is a powerful language"
print(str15.swapcase())

str16 = "His name is karmanya, karmanya is a liar"
print(str16.title()) # Capitalizes the first character for every word in the string




