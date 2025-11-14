# ----------------------------------------------
# CASE CONVERSION METHODS
# ----------------------------------------------

s = "hello world"

print("capitalize():", s.capitalize())          # Capitalize first letter
print("casefold():", "ß".casefold())            # Unicode aware lowercase
print("lower():", "HELLO".lower())              # Lowercase
print("swapcase():", "HeLLo".swapcase())        # Swap case
print("title():", "hello world python".title()) # Title case
print("upper():", "hello".upper())              # Uppercase


# ----------------------------------------------
# ALIGNMENT METHODS
# ----------------------------------------------

s = "hello"

print("center():", s.center(10, "-"))      # Center align
print("ljust():", s.ljust(10, "*"))        # Left justify
print("rjust():", s.rjust(10, "*"))        # Right justify
print("expandtabs():", "a\tb\tc".expandtabs(4))  # Tabs to spaces
print("zfill():", "42".zfill(5))           # Zero fill


# ----------------------------------------------
# SPLIT & JOIN METHODS
# ----------------------------------------------

s = "   hello world   "
t = "hello-world-python"

print("lstrip():", s.lstrip())                     # Remove leading spaces
print("rstrip():", s.rstrip())                     # Remove trailing spaces
print("strip():", s.strip())                       # Remove both sides

print("rsplit():", t.rsplit("-", 1))               # Split from right
print("split():", t.split("-"))                    # Split normally

multi = "line1\nline2\nline3"
print("splitlines():", multi.splitlines())         # Split by newline

print("partition():", t.partition("-"))            # First occurrence
print("rpartition():", t.rpartition("-"))          # Last occurrence

items = ["apple", "banana", "cherry"]
print("join():", ", ".join(items))                 # Join with separator

print("removeprefix():", "Mr.King".removeprefix("Mr."))
print("removesuffix():", "document.pdf".removesuffix(".pdf"))


# ----------------------------------------------
# BOOLEAN STRING METHODS (return True/False)
# ----------------------------------------------

print("isalnum():", "abc123".isalnum())
print("isalpha():", "hello".isalpha())
print("isdigit():", "12345".isdigit())
print("islower():", "hello".islower())
print("isnumeric():", "⑤".isnumeric())            # Unicode numeric
print("isspace():", "   ".isspace())
print("istitle():", "Hello World".istitle())
print("isupper():", "HELLO".isupper())
print("isascii():", "hello!".isascii())
print("isdecimal():", "123".isdecimal())
print("isidentifier():", "my_var".isidentifier())
print("isprintable():", "hello\n".isprintable())   # newline = not printable


# ----------------------------------------------
# FIND & REPLACE METHODS
# ----------------------------------------------

s = "hello world hello"

print("count():", s.count("hello"))                  # Count occurrences
print("find():", s.find("world"))                    # Find index
print("index():", s.index("hello"))                  # Index (raises error if not found)
print("replace():", s.replace("hello", "hi", 1))     # Replace once
print("rfind():", s.rfind("hello"))                  # Find from right
print("rindex():", s.rindex("hello"))                # Index from right

print("startswith():", s.startswith("hello"))
print("endswith():", s.endswith("hello"))


# ----------------------------------------------
# TRANSLATION METHODS
# ----------------------------------------------

# maketrans + translate
trans_table = str.maketrans({"a": "1", "e": "2", "i": "3"})
print("translate():", "hacker".translate(trans_table))
