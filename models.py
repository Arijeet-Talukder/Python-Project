class Account:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.transactions = []  

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        self.transactions.append("Deposit: " + str(amount))
        return True

    def withdraw(self, amount):
        if amount <= 0:
            return False
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
