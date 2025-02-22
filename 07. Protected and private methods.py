class BankAccount:
    MIN_BALANCE = 100  # Static attribute

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            self.__log_transaction("deposit", amount)
        else:
            print("Deposit amount must be positive.")

    def _is_valid_amount(self, amount):
        return amount > 0

    def __log_transaction(self, transaction_type, amount):
        print(
            f"Logging {transaction_type} of {amount}. New Balance: $ {self._balance}.")

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5


account = BankAccount("Alice", 500)
account.deposit(200)  # Output: Alice deposited 200. New balance: 700

# account.__is_valid_amount(200)  # Output: AttributeError
# account.__log_transaction("deposit", 200)  # Output: AttributeError

print(BankAccount.is_valid_interest_rate(3))  # Output: True
print(BankAccount.is_valid_interest_rate(6))  # Output: False

# In this example, the _is_valid_amount method is a protected method that checks if a given amount is valid for deposit. It can be accessed within the class and by subclasses, but it is not intended to be accessed from outside the class. The __log_transaction method is a private method that logs the transaction details. It can only be accessed within the class itself.
#
# In summary, the main differences between protected and private methods in Python are:
#
# 1. **Access Level**:
#    - Protected methods (prefixed with a single underscore `_`) can be accessed within the class and by subclasses.
#    - Private methods (prefixed with a double underscore `__`) can only be accessed within the class itself.
#
# 2. **Intended Use**:
#    - Protected methods are intended to be used by subclasses, allowing for inheritance and extension of functionality.
#    - Private methods are intended for internal use only, encapsulating functionality that should not be exposed to subclasses or external code.
