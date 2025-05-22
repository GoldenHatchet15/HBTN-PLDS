class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds or invalid amount!")

    @property  # Getter method
    def balance(self):
        return self.__balance

# Creating an object
account = BankAccount()

# Performing transactions
account.deposit(500)
account.withdraw(200)

# Checking balance
print(f"Current balance: ${account.balance}")  # Output: Current balance: $300
