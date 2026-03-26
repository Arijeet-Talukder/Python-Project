from __future__ import annotations
from rich.console import Console
from rich.table import Table

class CLI:
  def __init__(self) -> None:
        self.console = Console()
  def print_menu(self) -> None:
        self.console.print("\n------ Banking System ------")
        self.console.print("1. Create Account")
        self.console.print("2. Deposit")
        self.console.print("3. Withdraw")
        self.console.print("4. Transfer")
        self.console.print("5. List Accounts")
        self.console.print("6. Search Account")
        self.console.print("7. Delete Account")
        self.console.print("8. Report")
        self.console.print("9. Exit")
        
#features to be implemented here in the future due to uncertainty in naming functions.

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
                    self.console.print("Exiting... Goodbye!")
                    break
            case _:
                    self.console.print("Invalid choice!")
run_cli = CLI()
run_cli.run()