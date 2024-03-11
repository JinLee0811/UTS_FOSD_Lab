class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"\n\nDeposit successful. Your balance is now {self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"\n\nWithdrawal successful. Your balance is now {self.balance}.")
        else:
            print("\n\nInsufficient funds.")

    def check_balance(self):
        print(f"\n\nYour current balance is {self.balance}.")


def main():
    print("Welcome to the UTS Banking Program!")

    while True:
        print("Choose an option:")
        print("d. Deposit")
        print("w. Withdraw")
        print("s. Show Balance")
        print("x. Exit")

        choice = input("Enter your choice (d~x): ")

        if choice == "d":
            deposit_amount = float(input("Enter the deposit amount: "))
            account.deposit(deposit_amount)
        elif choice == "w":
            withdraw_amount = float(input("Enter the withdrawal amount: "))
            account.withdraw(withdraw_amount)
        elif choice == "s":
            account.check_balance()
        elif choice == "x":
            print("\nThank you for using the UTS Banking Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between d and x.")


if __name__ == "__main__":
    account = Account(1000.00)
    main()
