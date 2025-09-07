# Python - Inner Classes
# ✅ Definition:

# A class defined inside another class.

# Helps logically group classes and hide details.

# 📝 Notes:

# Often used when the inner class is only useful for the outer class.

# Provides better encapsulation.


class University:
    def __init__(self, name):
        self.name = name
    
    class Department:
        def __init__(self, dept_name):
            self.dept_name = dept_name

uni = University("Pace University")
dept = uni.Department("Cybersecurity")
print(uni.name)          # Pace University
print(dept.dept_name)    # Cybersecurity
