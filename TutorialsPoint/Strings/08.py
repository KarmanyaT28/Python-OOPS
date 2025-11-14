# String Formatting


name = "TutorialsPoint"
print("Welcome to %s!" % name)

str = "Welcome to {}"
print(str.format("TutorialsPoint"))


item1_price = 2500
item2_price=300

total = f'Total: {item1_price} + {item2_price}'
total1 = f'Total: {item1_price + item2_price}'
print(total)
print(total1)