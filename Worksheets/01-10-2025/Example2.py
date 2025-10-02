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