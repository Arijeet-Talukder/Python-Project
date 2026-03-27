from __future__ import annotations
from rich.console import Console
from rich.table import Table

class CLI:
  def __init__(self) -> None:
        self.console = Console()
  def print_menu(self) -> None:
        self.console.print("\n[bold blue]------ Banking System ------[/bold blue]")
        self.console.print("1. Create Account")
        self.console.print("2. Deposit")
        self.console.print("3. Withdraw")
        self.console.print("4. Transfer")
        self.console.print("5. List Accounts")
        self.console.print("6. Search Account")
        self.console.print("7. Delete Account")
        self.console.print("8. Report")
        self.console.print("9. Exit")
        
  def create_account(self) -> None:
        name = input("Enter name: ").strip()
        try:
            balance = float(input("Enter initial balance: "))
        except ValueError:
            self.console.print("Invalid amount!")
            return

        acc = self.manager.create_account(name, balance)
        self.console.print(f"Account created! Acc No: {acc.acc_no}")

  def deposit(self) -> None:
        try:
            acc_no = int(input("Account number: "))
            amount = float(input("Amount: "))
            self.manager.deposit(acc_no, amount)
            self.console.print("Deposit successful!")
        except Exception as e:
            self.console.print(f"Error: {e}")

  def withdraw(self) -> None:
        try:
            acc_no = int(input("Account number: "))
            amount = float(input("Amount: "))
            self.manager.withdraw(acc_no, amount)
            self.console.print("Withdraw successful!")
        except Exception as e:
            self.console.print(f"Error: {e}")

  def transfer(self) -> None:
        try:
            from_acc = int(input("From Account: "))
            to_acc = int(input("To Account: "))
            amount = float(input("Amount: "))
            self.manager.transfer(from_acc, to_acc, amount)
            self.console.print("Transfer successful!")
        except Exception as e:
            self.console.print(f"Error: {e}")

  def list_accounts(self) -> None:
        accounts = self.manager.get_all_accounts()

        if not accounts:
            self.console.print("No accounts found!")
            return

        table = Table(title="Accounts")
        table.add_column("Acc No", justify="right")
        table.add_column("Name")
        table.add_column("Balance", justify="right")

        for acc in accounts:
            table.add_row(str(acc.acc_no), acc.name, f"{acc.balance:.2f}")

        self.console.print(table)

  def search_account(self) -> None:
        keyword = input("Enter name or account number: ").strip()
        results = self.manager.search(keyword)

        if not results:
            self.console.print("No accounts found!")
            return

        table = Table(title="Search Results")
        table.add_column("Acc No", justify="right")
        table.add_column("Name")
        table.add_column("Balance", justify="right")

        for acc in results:
            table.add_row(str(acc.acc_no), acc.name, f"{acc.balance:.2f}")

        self.console.print(table)

  def delete_account(self) -> None:
        try:
            acc_no = int(input("Account number: "))
            self.manager.delete_account(acc_no)
            self.console.print("Account deleted!")
        except Exception as e:
            self.console.print(f"Error: {e}")

  def report(self) -> None:
        total = self.manager.total_balance()
        top = self.manager.top_accounts(3)

        self.console.print("\n--- REPORT ---")
        self.console.print(f"Total Balance: {total}")

        table = Table(title="Top Accounts")
        table.add_column("Acc No", justify="right")
        table.add_column("Name")
        table.add_column("Balance", justify="right")

        for acc in top:
            table.add_row(str(acc.acc_no), acc.name, f"{acc.balance:.2f}")

        self.console.print(table)

  def run(self) -> None:
     while True:
        self.print_menu()
        choice: str = input("Choose an option (1 - 9): ").strip()

        match choice:
            case "1":
                    self.console.print("Creating account...")
            case "2":
                    self.console.print("Depositing funds...")
            case "3":
                    self.console.print("Withdrawing funds...")
            case "4":
                    self.console.print("Transferring funds...")
            case "5":
                    self.console.print("Listing accounts...")
            case "6":
                    self.console.print("Searching account...")
            case "7":
                    self.console.print("Deleting account...")
            case "8":
                    self.console.print("reporting...")
            case "9":
                    self.console.print("[bold red]Exiting... Goodbye![/bold red]")
                    break
            case _:
                    self.console.print("[bold red]Invalid choice![/bold red]")
run_cli = CLI()
run_cli.run()