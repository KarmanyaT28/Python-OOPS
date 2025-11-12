# Keyword only argument
# Those arguments that must be specified by their name while
# calling the function is known as Keyword-only arguments


def posFun(*,num1,num2,num3):
    print(num1 * num2 * num3)


print("Evaluating keyword-only arguments: ")
posFun(num1=6,num2=7,num3=8)