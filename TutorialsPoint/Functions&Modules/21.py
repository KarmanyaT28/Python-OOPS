# Python - Arbitrary or Variable-length Arguments

# sum of numbers
def add(*args):
   s=0
   for x in args:
      s=s+x
   return s
result = add(10,20,30,40)
print (result)

result = add(1,2,3)
print (result)

# Another Example


def avg(first, *rest):
    second = max(rest)
    return (first + second) / 2


result = avg(40, 30, 50, 25)
print(result)


