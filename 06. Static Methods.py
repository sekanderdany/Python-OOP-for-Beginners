# Static Sethods
# Static methods are methods that belong to the class rather than any particular instance. They can be called on the class itself, and they do not require an instance of the class to be created. Static methods do not have access to the instance (self) or class (cls) variables.
#
# To define a static method in Python, you use the @staticmethod decorator.
#
# Here's an example:

# static vs instance methods

class BankAccount:
    MIN_BALANCE = 100  # Static attribute

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.owner} deposited {amount}. New balance: {self._balance}")
        else:
            print("Deposit amount must be positive.")

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5


account = BankAccount("Alice", 500)
account.deposit(200)  # Output: Alice deposited 200. New balance: 700

print(BankAccount.is_valid_interest_rate(3))  # Output: True
print(BankAccount.is_valid_interest_rate(6))  # Output: False

# In this example, the is_valid_interest_rate method is a static method that checks if a given interest rate is valid. It can be called on the class itself without needing an instance of the class.
