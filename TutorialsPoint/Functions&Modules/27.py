# Function Annotations

# The function annotation feature of Python enables you to add additional explanatory metadata
# about the arguments declared in a function definition, and also the return data type.
# They are not considered by Python interpreter while executing the function.
# They are mainly for the Python IDEs for providing a detailed documentation to the programmer.


def myfunction(a: int, b: int):
    c = a + b
    return c


print(myfunction(10, 20))
print(myfunction("Hello ", "Python"))



def myfunction1(a: int, b: int) -> int:
   c = a+b
   return c
print(myfunction1(56,88))
print(myfunction1.__annotations__)



def total(x : 'marks in Physics', y: 'marks in chemistry'):
   return x+y
print(total(86, 88))
print(total.__annotations__)




def myfunction4(*args: "arbitrary args", **kwargs: "arbitrary keyword args") -> int:
   pass
print (myfunction4.__annotations__)



def division(num: dict(type=float, msg='numerator'), den: dict(type=float, msg='denominator')) -> float:
   return num/den
print (division.__annotations__)