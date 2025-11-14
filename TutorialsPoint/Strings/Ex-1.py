# Python program to find number of vowels in a given string.

print("Enter your string: ")
str = input()

l1 = ['a','e','i','o','u']

count = 0

for character in str:
    if character in l1:
        count += 1
    else:
        count +=0

print(count)

# mystr = "All animals are equal. Some are more equal"
# vowels = "aeiou"
# count=0
# for x in mystr:
#    if x.lower() in vowels: count+=1
# print ("Number of Vowels:", count)