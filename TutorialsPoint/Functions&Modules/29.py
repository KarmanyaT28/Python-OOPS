Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   global Money
   Money = Money + 1
print (Money)
AddMoney()
print (Money)


# we accessed the value of the local variable Money before setting it, so an UnboundLocalError is the result. 