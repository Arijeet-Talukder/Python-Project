from models import Account

class BankManager:

    def __init__(self):
        self.accounts = []

    def create_account(self, name, balance):
        acc_no = len(self.accounts) + 1
        acc = Account(acc_no, name, balance)
        self.accounts.append(acc)
        return acc


    def deposit(self, acc_no, amount):
        for acc in self.accounts:
            if acc.acc_no == acc_no:
                acc.balance = acc.balance + amount
                return True, "Deposit successful"

        return False, "Account not found"


    def withdraw(self, acc_no, amount):
        for acc in self.accounts:
            if acc.acc_no == acc_no:
                if amount > acc.balance:
                    return False, "Not enough balance"

                acc.balance = acc.balance - amount
                return True, "Withdraw successful"

        return False, "Account not found"

    def transfer(self, from_acc, to_acc, amount):
        sender = None
        receiver = None

        for acc in self.accounts:
            if acc.acc_no == from_acc:
                sender = acc
            if acc.acc_no == to_acc:
                receiver = acc

        if sender is None:
            return False, "Sender not found"

        if receiver is None:
            return False, "Receiver not found"

        if amount > sender.balance:
            return False, "Not enough balance"

        sender.balance = sender.balance - amount
        receiver.balance = receiver.balance + amount

        return True, "Transfer successful"
    
    def get_all_accounts(self):
        return self.accounts


    def search(self, keyword):
        result = []

        for acc in self.accounts:
            name = acc.name.lower()
            key = keyword.lower()

            if str(acc.acc_no) == key or key in name:
                result.append(acc)

        return result


    def delete_account(self, acc_no):
        for acc in self.accounts:
            if acc.acc_no == acc_no:
                self.accounts.remove(acc)
                return True, "Account deleted"

        return False, "Account not found"


    def total_balance(self):
        total = 0

        for acc in self.accounts:
            total = total + acc.balance

        return total

    def top_accounts(self, count=3):
        return sorted(self.accounts, key=lambda acc: acc.balance, reverse=True)[:count]