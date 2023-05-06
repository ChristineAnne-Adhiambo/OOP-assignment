class Account:
    bank = "KCB Bank"

    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        self.balance += amount
        return f"Amount {amount} deposited. New balance: {self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Amount {amount} withdrawn. New balance: {self.balance}"
        else:
            return "Insufficient funds."

    def get_account_info(self):
        return f"Account Number: {self.account_number}\nAccount Type: {self.account_type}\nBalance: {self.balance}"
