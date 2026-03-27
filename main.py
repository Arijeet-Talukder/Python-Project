from manager import BankManager
from storage import Storage
from cli import CLI


def main() -> None:
    manager = BankManager()
    storage = Storage()   

    manager.accounts = storage.load()

    app = CLI(manager)
    app.run()

    storage.save(manager.accounts)


if __name__ == "__main__":
    main()