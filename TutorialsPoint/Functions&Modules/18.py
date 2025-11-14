# Keyword Only

def intr(amt, *, rate):
    val = amt * rate / 100
    return val

# To make an argument keyword-only, put the astreisk (*) before it while creating the user-defined function.


interest = intr(1000, rate=10)
# interest = intr(1000, 10)
print(interest)