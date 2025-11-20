# Exception Handling
from pandas.io.pytables import IndexCol

# try except


a = input("Enter a number: ")

print(f"Multiplication table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a) * i}")
except Exception as e:
    print(e)



try:
    num = int(input("Enter a number: "))
    a = [6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Number entered is out of range.")


print("Some important lines of code")
print("Do not remove these lines from the code")
