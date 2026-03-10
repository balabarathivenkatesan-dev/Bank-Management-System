class Account:

    def __init__(self, acc_no, holder_name, balance):
        self.acc_no = acc_no
        self.holder_name = holder_name
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully")

    def display(self):
        print(f"Account Number : {self.acc_no}")
        print(f"Holder Name    : {self.holder_name}")
        print(f"Balance        : {self.balance}")


class Bank:

    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_no, name, balance):

        if acc_no in self.accounts:
            print("Account already exists")
        else:
            acc = Account(acc_no, name, balance)
            self.accounts[acc_no] = acc
            print("Account created successfully")

    def delete_account(self, acc_no):

        if acc_no in self.accounts:
            del self.accounts[acc_no]
            print("Account deleted successfully")
        else:
            print("Account does not exist")

    def update_account(self, acc_no, name=None, balance=None):

        if acc_no in self.accounts:

            if name:
                self.accounts[acc_no].holder_name = name

            if balance:
                self.accounts[acc_no].balance = float(balance)

            print("Account updated successfully")

        else:
            print("Account does not exist")

    def account_details(self, acc_no):

        if acc_no in self.accounts:
            self.accounts[acc_no].display()
        else:
            print("Account not found")

    def list_accounts(self):

        if not self.accounts:
            print("No accounts available")
        else:
            for acc in self.accounts.values():
                acc.display()
                print("-------------------------")

    def deposit(self, acc_no, amount):

        if acc_no in self.accounts:
            self.accounts[acc_no].deposit(float(amount))
        else:
            print("Account does not exist")

    def withdraw(self, acc_no, amount):

        if acc_no in self.accounts:
            self.accounts[acc_no].withdraw(float(amount))
        else:
            print("Account does not exist")

    def view_balance(self, acc_no):

        if acc_no in self.accounts:
            print(f"Balance : {self.accounts[acc_no].balance}")
        else:
            print("Account does not exist")


class Menu:

    def __init__(self):
        self.bank = Bank()

    def run(self):

        while True:

            print("\nBank Management System")
            print("1.Create Account")
            print("2.Delete Account")
            print("3.Update Account")
            print("4.View Balance")
            print("5.View Account Details")
            print("6.List All Accounts")
            print("7.Deposit Amount")
            print("8.Withdraw Amount")
            print("9.Exit")
            print("-------------------------------------")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input")
                continue

            if choice == 1:
                acc = input("Enter account number: ")
                name = input("Enter holder name: ")
                bal = input("Enter balance: ")
                self.bank.create_account(acc, name, bal)

            elif choice == 2:
                acc = input("Enter account number: ")
                self.bank.delete_account(acc)

            elif choice == 3:
                acc = input("Enter account number: ")
                name = input("Enter new name (press enter to skip): ") or None
                bal = input("Enter new balance (press enter to skip): ") or None
                self.bank.update_account(acc, name, bal)

            elif choice == 4:
                acc = input("Enter account number: ")
                self.bank.view_balance(acc)

            elif choice == 5:
                acc = input("Enter account number: ")
                self.bank.account_details(acc)

            elif choice == 6:
                self.bank.list_accounts()

            elif choice == 7:
                acc = input("Enter account number: ")
                amt = input("Enter amount to deposit: ")
                self.bank.deposit(acc, amt)

            elif choice == 8:
                acc = input("Enter account number: ")
                amt = input("Enter amount to withdraw: ")
                self.bank.withdraw(acc, amt)

            elif choice == 9:
                print("Exiting system...")
                break

            else:
                print("Invalid choice")


m = Menu()
m.run()