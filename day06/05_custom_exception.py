class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise InsufficientFundsError("Withdrawal amount exceeds balance!")
        self.__balance -= amount

    def check_balance(self):
        return self.__balance

acc = BankAccount("Bob", 300)
try:
    acc.withdraw(500)
except InsufficientFundsError as e:
    print(e)
