# Finally Keyword

'''try:
    l = [1,2,3,4,5]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Something went wrong")

# finally:
#     print("I am always executed")

print("I am always executed")'''



# difference comes when you wrap all of this inside a function


def function1():
    try:
        l = [1, 2, 3, 4, 5]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Something went wrong")
        return 0

    finally:
        print("I am always executed")

    # print("I am always executed using print")

x = function1()
print(x)
