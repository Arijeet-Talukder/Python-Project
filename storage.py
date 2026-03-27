'''
Handles saving and loading accounts using CSV
'''
from __future__ import annotations
import csv
from models import Account

class Storage:
    def __init__(self, filename: str = "data.csv") -> None:
        self.filename = filename

    def save(self, accounts: list[Account]) -> None:
        try:
            with open(self.filename, mode="w", newline="") as file:
                writer = csv.writer(file)

                writer.writerow(["acc_no", "name", "balance"])

                for acc in accounts:
                    writer.writerow([acc.acc_no, acc.name, acc.balance])

        except Exception as e:
            print(f"Error saving data: {e}")

    def load(self) -> list[Account]:
        accounts: list[Account] = []

        try:
            with open(self.filename, mode="r") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    acc = Account(
                        int(row["acc_no"]),
                        row["name"],
                        float(row["balance"])
                    )
                    accounts.append(acc)

        except FileNotFoundError:
            
            pass
        except Exception as e:
            print(f"Error loading data: {e}")

        return accounts