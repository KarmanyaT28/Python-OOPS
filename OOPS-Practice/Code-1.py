class BankAccount:
    def __init__(self,owner_name, initial_balance=0):
        self.owner_name = owner_name
        self.__balance = initial_balance
        print(f"Account Created for {self.owner_name} with initial balance of {initial_balance}")


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} to {self.owner_name} with new balance of {self.__balance}")
            return True
        else:
            print(f"Deposit amount should be positive")
            return False

    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount} to {self.owner_name} with new balance of {self.__balance}")
            return True
        else:
            print(f"Withdrawal failed : Insufficient balance")
            return False


    def get_balance(self):
        return self.__balance




# 1. Create a new object (instance) of the BankAccount class
my_account = BankAccount("Alice Smith", 500)

print("\n--- Object Interaction ---")

# 2. Accessing a Public attribute (allowed)
print(f"Account Owner: {my_account.owner}")

# 3. Interacting using controlled methods (Encapsulation in action)
my_account.deposit(200)
my_account.withdraw(50)

# 4. Attempting to directly access/change the 'private' attribute (Discouraged/Fails clearly)
# Note: Python doesn't enforce strict privacy, but this signals intent and makes direct access awkward.
try:
    print(f"Attempting to read balance directly: {my_account.__balance}")
except AttributeError as e:
    print(f" Direct read failed (Encapsulation): {e}")

# 5. Using the safe getter method
current_balance = my_account.get_balance()
print(f" Balance read via getter method: ${current_balance}")