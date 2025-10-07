# Advanced Topic: Properties (Getters, Setters, and Deleters)
# In Day 1, we learned about Encapsulation using single/double underscores.
# Python('s preferred, more elegant way to implement controlled access
# (Getters and Setters) is using the @property decorator.)
#
# Why it matters for Cybersecurity: Properties allow you to add validation logic
# (Setters) or read-only controls (Getters) to attributes after they've
# been defined, preventing invalid or malicious values from corrupting your object's state.

class SecureUser:
    VALID_ROLES = {"auditor", "operator", "admin"}

    def __init__(self, username, role):
        self._username = username # Internal protected attribute
        self._role = None         # Internal storage for the property
        self.role = role          # Calls the setter method below

    # Getter: Defines how the attribute is READ
    @property
    def role(self):
        """This method runs when you access user.role"""
        return self._role

    # Setter: Defines how the attribute is WRITTEN
    @role.setter
    def role(self, new_role):
        """This method runs when you assign a value: user.role = '...'"""
        # Security Validation: Only allow valid roles to be set
        if new_role.lower() not in self.VALID_ROLES:
            raise ValueError(f"Invalid role '{new_role}'. Must be one of {self.VALID_ROLES}.")
        self._role = new_role.lower()

# Creating a user
admin = SecureUser("neo", "Admin")
print(f"User role: {admin.role}") # Accesses the @property getter

# Setting a valid new value (runs the setter with validation)
admin.role = "operator"

# Setting an invalid value (raises an exception)
try:
    admin.role = "super_admin"
except ValueError as e:
    print(f"ERROR: {e}")