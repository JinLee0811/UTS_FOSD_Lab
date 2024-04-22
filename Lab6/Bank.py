# 기존의 은행 어플에 계좌에 Type을 늘려서 (Savings, loan) 2개의 타입으로 각각 입금이 가능하며
# 해당 계좌간의 이체가 가능하도록 수정함.
# saviongs to loan 만 이체 가능


class Account:
    def __init__(self, account_type, balance):
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def show_balance(self):
        return f"{self.account_type} account has ${self.balance:.2f}"

    def transfer(self, target_account, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.withdraw(amount)
        target_account.deposit(amount)


class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def add_account(self, account_type, balance):
        self.accounts[account_type] = Account(account_type, balance)

    def get_account(self, account_type):
        return self.accounts.get(account_type, None)


class Bank:
    def __init__(self):
        self.customer = None

    def add_customer(self, customer):
        self.customer = customer

    def deposit(self, account_type, amount):
        account = self.customer.get_account(account_type)
        if account:
            account.deposit(amount)
            print("Deposit successful.")
        else:
            print(f"No {account_type} account found.")

    def withdraw(self, account_type, amount):
        account = self.customer.get_account(account_type)
        if account:
            try:
                account.withdraw(amount)
                print("Withdrawal successful.")
            except ValueError as e:
                print(e)
        else:
            print(f"No {account_type} account found.")

    def show_balance(self, account_type):
        account = self.customer.get_account(account_type)
        if account:
            print(account.show_balance())
        else:
            print(f"No {account_type} account found.")

    def transfer(self, source_account_type, target_account_type, amount):
        source_account = self.customer.get_account(source_account_type)
        target_account = self.customer.get_account(target_account_type)
        if source_account and target_account:
            try:
                source_account.transfer(target_account, amount)
                print("Transfer successful.")
            except ValueError as e:
                print(e)
        else:
            print("One or both accounts not found.")

    def system_menu(self):
        print("Welcome to the DeskBankApp system")
        while True:
            print("\nCustomer menu (d/w/t/s/x):")
            choice = input("Choose an option: ").lower()
            if choice == "d":
                account_type = input("Enter account type (savings/loan): ")
                amount = float(input("Enter the deposit amount: "))
                self.deposit(account_type, amount)
            elif choice == "w":
                account_type = input("Enter account type (savings/loan): ")
                amount = float(input("Enter the withdrawal amount: "))
                self.withdraw(account_type, amount)
            elif choice == "t":
                source = input("Enter the source account type (savings/loan): ")
                target = input("Enter the target account type (savings/loan): ")
                amount = float(input("Enter the transfer amount: "))
                self.transfer(source, target, amount)
            elif choice == "s":
                account_type = input("Enter account type (savings/loan): ")
                self.show_balance(account_type)
            elif choice == "x":
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please enter a valid command (d/w/t/s/x).")
                self.show_full_menu()

    def show_full_menu(self):
        print("Full menu:")
        print("d - Deposit")
        print("w - Withdraw")
        print("t - Transfer")
        print("s - Show balance")
        print("x - Exit")


if __name__ == "__main__":
    bank = Bank()
    customer = Customer("John Smith")
    customer.add_account("savings", 1000.00)
    customer.add_account("loan", 2000.00)
    bank.add_customer(customer)

    bank.system_menu()
