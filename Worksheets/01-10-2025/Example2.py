# Core Topic: Encapsulation (Beginner Level)
# Encapsulation is the concept of bundling data (attributes) and the methods (functions)
# that operate on that data into a single unit (the class).
# It also includes controlling access to the data.
#
# In Python, we achieve a soft form of access control using naming conventions:
#
# Public Attributes: Accessible directly from outside the class (e.g., self.ip_address).
# You can and should change these if needed.
#
# Protected Attributes: Indicated by a single leading underscore (e.g., _config).
# This is a convention, signaling to other programmers that these attributes shouldn('t be accessed directly, '
# though Python doesn')t strictly prevent it.
#
# Private Attributes: Indicated by two leading underscores (e.g., __secret_key).
# Python performs name mangling on these, making them harder to access from outside,
# enforcing a stricter level of privacy.



class UserAccount:
    def __init__(self, username, password_hash):
        self.username = username             # Public
        self._login_attempts = 0            # Protected (convention for internal use)
        self.__password_hash = password_hash # Private (name-mangled)

    def login(self, attempt_hash):
        if attempt_hash == self.__password_hash:
            print(f"Login successful for {self.username}.")
            self._login_attempts = 0
            return True
        else:
            self._login_attempts += 1
            print(f"Login failed. Attempt count: {self._login_attempts}")
            return False

# Create an object
user = UserAccount("alice", "d2b4f...")

# Direct access (possible but discouraged for protected/private)
print(user.username)         # OK, Public
print(user._login_attempts)  # Discouraged, but works (Protected)

# Attempt to access the "private" attribute directly (fails standardly)
try:
    print(user.__password_hash)
except AttributeError as e:
    print(f"Accessing private failed: {e}")

# Accessing the password hash is done via the method (Encapsulation in action)
user.login("wrong_hash")