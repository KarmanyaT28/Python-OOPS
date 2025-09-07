# Python - Wrapper Classes
# ✅ Definition:

# A wrapper class is a class that encapsulates another object to extend or restrict its behavior.

# 📝 Notes:

# In Java/C++, wrapper classes wrap primitive types (int → Integer).

# In Python, everything is already an object, so wrapper classes are used to add extra functionality around existing objects.


class IntWrapper:
    def __init__(self, value):
        self.value = value
    
    def double(self):
        return self.value * 2

num = IntWrapper(15)
print(num.double())   # 30




class ListWrapper:
    def __init__(self, data):
        self.data = data
    
    def get_first(self):
        return self.data[0]

wrapped = ListWrapper([10, 20, 30])
print(wrapped.get_first())  # 10
