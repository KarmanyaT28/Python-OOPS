var1 = 'hello world!'
var2 = "python Programming"


print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])


var3 = 'Hello World!'
print("Updated String:-", var3[:6] + 'Python')

# Python Backslash Escape Sequence Reference
# ------------------------------------------
# \a    -> Bell / Alert (Hex: 0x07)
# \b    -> Backspace (Hex: 0x08)
# \cx   -> Control-x (Ctrl + x)
# \C-x  -> Control-x (alternative form)
# \e    -> Escape (Hex: 0x1b)
# \f    -> Formfeed (Hex: 0x0c)
# \M-\C-x -> Meta-Control-x
# \n    -> Newline (Hex: 0x0a)
# \nnn  -> Octal value (n ranges 0–7)
# \r    -> Carriage Return (Hex: 0x0d)
# \s    -> Space (Hex: 0x20)
# \t    -> Horizontal Tab (Hex: 0x09)
# \v    -> Vertical Tab (Hex: 0x0b)
# \x    -> Character x literally if not forming a hex code
# \xnn  -> Hexadecimal value (0–9, a–f, A–F)


# String Formatting Operator

print ("My name is %s and weight is %d kg!" % ('Zara', 21))



# Double Quotes in Python Strings

var4 = 'Welcome to Python Tutorial" from TutorialsPoint'
print("var4:",var4)


var5 = "Welcome to 'Python Tutorial' from TutorialsPoint"
print("var5:", var5)


var6 = '''Welcome to TutorialsPoint'''
print("var6:", var6)

var7 = """Welcome to TutorialsPoint"""
print("var7:", var7)


var8 = '''
Welcome to
python tutorial
from tutorialspoint
'''

print("var8:", var8)




#print ("Hello"-"World") #Error unsupported operand type


print(var2.capitalize())

print(var2.casefold())

print(var2.center(6,'a'))