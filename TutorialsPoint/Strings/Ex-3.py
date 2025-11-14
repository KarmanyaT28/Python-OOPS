print("Enter your string")
string1 = input()
newstring1 = "" # Initialize the new string as empty

for character in string1:
    # Check if the character is NOT a digit
    if not character.isdigit():
        # Only add the non-digit characters to the new string
        newstring1 += character

print(newstring1)