# Encapsulation

class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance


# account = BadBankAccount(0.0)

# account.balance = -1
# print(account.balance)  # Output: -1


class BankAccount:
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount


account = BankAccount()
account.deposit(1.99)
print(account.balance)  # Output: 1.99
account.withdraw(1.00)
print(account.balance)  # Output: 100.99
account.withdraw(100)  # Output: ValueError: Insufficient funds

# In this example, the BankAccount class encapsulates the balance attribute and provides methods to deposit and withdraw money. The balance attribute is private (prefixed with an underscore), and it can only be accessed through the public deposit and withdraw methods. This ensures that the balance cannot be set to an invalid value directly, thus maintaining the integrity of the account.
# Encapsulation is a fundamental concept in object-oriented programming that refers to the bundling of data (attributes) and methods (functions) that operate on that data within a single unit, typically a class. It restricts direct access to some of an object's components and can prevent the accidental modification of data. Encapsulation helps to protect the internal state of an object and ensures that it can only be modified in controlled ways.
