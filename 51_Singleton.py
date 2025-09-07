# Python - Singleton Class
# ✅ Definition:

# A class designed so that only one instance exists throughout the program.

# 📝 Notes:

# Used in logging, configuration management, database connections.

# Prevents multiple objects from being created.


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:   # If no instance exists
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()

print(a is b)  # True → same object
