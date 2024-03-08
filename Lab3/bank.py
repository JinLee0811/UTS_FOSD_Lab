class Customer:
    def __init__(self, name, account_number, password, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.password = password

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


# 사용자 정보 등록
customer_list = [
    Customer("Jin", "1234", "0000", 1000.00),
    Customer("Kim", "9876", "0000", 1500.50),
    # 추가적으로 원하는 고객 정보 등록
]


def find_customer(name, password, account_number):
    for customer in customer_list:
        if (
            customer.name == name
            and customer.account_number == account_number
            and customer.password == password
        ):
            return customer
    else:
        print("your account/password number is wrong")
        return main()


def main():
    print("Welcome to the UTS Banking Program!")

    # 사용자 정보 확인
    name = input("Enter your name: ")
    account_number = input("Enter your account number: ")
    password = input("Enter your account password: ")
    customer = find_customer(name, password, account_number)

    if customer:
        print(f"Hello, {customer.name}! Your account balance is {customer.balance}.")

        # 입금, 출금, 잔액 확인 반복
        while True:
            print("\n\nHello! Mr/Ms {0} This is UTS bank".format(customer.name))
            print("Choose an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                deposit_amount = float(input("Enter the deposit amount: "))
                customer.deposit(deposit_amount)
            elif choice == "2":
                withdraw_amount = float(input("Enter the withdrawal amount: "))
                customer.withdraw(withdraw_amount)
            elif choice == "3":
                customer.check_balance()
            elif choice == "4":
                print("\nThank you for using the UTS Banking Program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    else:
        print("Customer not found. Exiting program.")


if __name__ == "__main__":
    main()
