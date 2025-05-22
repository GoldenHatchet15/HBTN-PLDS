from abc import ABC, abstractmethod

class BankAccount(ABC):  # Abstract Base Class
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  # Private attribute

    @property
    def balance(self):
        """Getter: Returns the current balance (read-only)"""
        return self._balance

    @balance.setter
    def balance(self, amount):
        """Setter: Ensures only valid balances can be set"""
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self._balance = amount  # Updates balance only if valid

    @balance.deleter
    def balance(self):
        """Deleter: Resets the balance to 0"""
        print(f"Deleting balance for {self.owner}...")
        self._balance = 0

    @abstractmethod
    def withdraw(self, amount):
        """Abstract method to enforce withdrawal logic"""
        pass

    @abstractmethod
    def deposit(self, amount):
        """Abstract method to enforce deposit logic"""
        pass

# Subclass 1: Savings Account
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        """Withdraws money but enforces a minimum balance of $100"""
        if self._balance - amount < 100:
            raise ValueError("Cannot withdraw! Minimum balance of $100 required.")
        self._balance -= amount
        return f"Withdrawn ${amount}. New balance: ${self._balance}"

    def deposit(self, amount):
        """Adds money to the savings account"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self._balance += amount
        return f"Deposited ${amount}. New balance: ${self._balance}"

# Subclass 2: Checking Account
class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        """Withdraws money but prevents overdrafts"""
        if amount > self._balance:
            raise ValueError("Insufficient funds!")
        self._balance -= amount
        return f"Withdrawn ${amount}. New balance: ${self._balance}"

    def deposit(self, amount):
        """Deposits money into the checking account"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self._balance += amount
        return f"Deposited ${amount}. New balance: ${self._balance}"

# Usage
savings = SavingsAccount("Alice", 500)
print(savings.deposit(200))  # ✅ Output: Deposited $200. New balance: $700
print(savings.withdraw(300))  # ✅ Works fine
print(savings.balance)  # Output: 400

checking = CheckingAccount("Bob", 1000)
print(checking.withdraw(800))  # ✅ Works fine
print(checking.deposit(500))  # ✅ Deposited $500. New balance: $700

# Trying to withdraw too much from savings
try:
    print(savings.withdraw(350))  # ❌ ValueError: Minimum balance of $100 required.
except ValueError as e:
    print(e)

# Trying to instantiate abstract class (This will fail)
try:
    acc = BankAccount("John", 500)  # ❌ TypeError: Can't instantiate abstract class
except TypeError as e:
    print(e)

# Accessing owners name 
print(savings.owner)  # Output: Alice
print(checking.owner)  # Output: Bob