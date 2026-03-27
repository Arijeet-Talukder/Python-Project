# models.py

class Account:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.transactions = []   # optional transaction history

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append("Deposit: " + str(amount))

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        else:
            self.balance = self.balance - amount
            self.transactions.append("Withdraw: " + str(amount))
            return True

    def Dictionary(self):
        val = {}
        val["acc_no"] = self.acc_no
        val["name"] = self.name
        val["balance"] = self.balance
        val["transactions"] = self.transactions
        return val