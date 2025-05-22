class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner  # Public attribute (accessible from outside)
        self.__balance = balance  # Private attribute (hidden from direct access)
    
    def deposit(self, amount):  # Public method to modify private data
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited. New balance: ${self.__balance}")
    
    def withdraw(self, amount):  # Public method to modify private data
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount.")
    
    def get_balance(self):  # Public method to retrieve private data
        return self.__balance

# Creating an object (a bank account)
account = BankAccount("Alice", 1000)

# Accessing public attribute
print(account.owner)  # Output: Alice

# Accessing private attribute directly (this will cause an error)
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

# Using methods to interact with private data
account.deposit(500)   # Output: $500 deposited. New balance: $1500
account.withdraw(300)  # Output: $300 withdrawn. New balance: $1200
print(account.get_balance())  # Output: 1200



#Why Use Encapsulation?
#Protects sensitive data from being accidentally modified.
#Ensures data is changed only through controlled methods.
#Improves code security and reliability.