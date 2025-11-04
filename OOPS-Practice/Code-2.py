# --- Parent Class (from Day 1) ---

class BankAccount:
    """The base class for all account types."""

    def __init__(self, owner_name, initial_balance=0):
        self.owner = owner_name
        self.__balance = initial_balance
        print(f"Base Account created for {self.owner}.")

    def deposit(self, amount):
        """Adds funds to the account."""
        if amount > 0:
            self.__balance += amount
            print(f"Base Deposit: ${amount}. New Balance: ${self.get_balance()}")
            return True
        return False

    def get_balance(self):
        """Getter for the encapsulated balance."""
        return self.__balance


# --- Child Class (Inheritance in Action) ---

# SavingsAccount is the subclass, BankAccount is the superclass
class SavingsAccount(BankAccount):
    """
    A specialized account that adds an interest rate and a fee rule.
    It inherits methods like deposit() and get_balance().
    """

    def __init__(self, owner_name, initial_balance=0, interest_rate=0.01):
        # 1. Use super() to call the constructor of the parent class (BankAccount)
        super().__init__(owner_name, initial_balance)

        # 2. Add new attributes specific to SavingsAccount
        self.interest_rate = interest_rate
        print(f"Savings Account setup complete with rate: {self.interest_rate * 100}%.")

    def apply_interest(self):
        """A new method specific to the SavingsAccount."""
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)  # Reusing the inherited deposit method!
        print(f"Interest applied: ${interest:.2f}.")

    def withdraw(self, amount):
        """
        Overrides the parent's withdraw method to add a specific rule (e.g., fee).
        """
        # Additional rule: Check if withdrawal is below a certain minimum
        if self.get_balance() - amount < 100:
            print("🚫 Warning: Withdrawal will drop balance below minimum threshold ($100).")

        # Call the parent's (BankAccount's) withdraw logic
        # Note: Since the parent's __balance is encapsulated, we must implement
        # a version of withdraw in the subclass or access it indirectly.
        # For simplicity, let's assume direct balance access for this example:
        if 0 < amount <= self.get_balance():
            # In a real scenario, we'd need a public 'withdraw' in BankAccount
            # or a way to modify the private balance.
            # Since BankAccount didn't have a public withdraw, we define it fully here:
            new_balance = self.get_balance() - amount

            # --- IMPORTANT: Direct private access workaround for demonstration ---
            # To modify the parent's private attribute, the convention is name mangling:
            self._BankAccount__balance = new_balance

            print(f"Savings Withdrawal: ${amount}. New Balance: ${self.get_balance()}")
            return True
        else:
            print("Savings Withdrawal failed: Insufficient funds or invalid amount.")
            return False


# --- Object Creation and Interaction ---

print("--- 1. Creating the SavingsAccount Object ---")
# Creates a SavingsAccount object, which internally calls the BankAccount constructor
alice_savings = SavingsAccount("Alice Johnson", initial_balance=1000, interest_rate=0.05)

print("\n--- 2. Inherited & New Methods ---")
# Uses the inherited deposit method
alice_savings.deposit(500)

# Uses the new method specific to the subclass
alice_savings.apply_interest()

print("\n--- 3. Overridden Method ---")
# Uses the overridden withdraw method with the new warning logic
alice_savings.withdraw(1400)  # This should succeed but warn
alice_savings.withdraw(200)  # This should fail