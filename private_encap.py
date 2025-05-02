class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance  # Accessing private member internally

# Usage
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(300)
print(account.__balance)
#print(account.get_balance())  # Works: 1200

