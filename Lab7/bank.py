from config import DTF, NOW
from customer import Customer


class Bank:
    def __init__(self):
        self.customers = []
        self.add_customers()

    def main(self):
        self.menu()

    def add_customers(self):
        try:
            num_customers = int(input("How many customer do you want to add? : "))
            for _ in range(num_customers):
                self.customers.append(Customer())
        except ValueError:
            print("Please enter a valid number of customers.")

    def read_choice(self):
        print("Bank menu (L/V/X): ", end="")
        return input().strip().upper()

    def customer(self, name):
        for c in self.customers:
            if c.match(name):
                return c
        return None

    def read_name(self):
        print("Enter Login Name: ", end="")
        return input().strip()

    def login(self):
        check = self.customer(self.read_name())
        if check:
            check.customerMenu()
        else:
            print("Customer does not exist")

    def view(self):
        for customer in self.customers:
            print(customer)

    def menu(self):
        print("Bank menu: " + NOW.strftime(DTF))  # current time
        while True:
            choice = self.read_choice()
            if choice == "X":
                break
            elif choice == "L":
                self.login()
            elif choice == "V":
                self.view()
            else:
                self.help()
        print("Done")

    def help(self):
        print("Menu options")
        print("L = Login into customer menu")
        print("V = View all customers")
        print("X = exit")


# Running the main function
bank = Bank()
bank.main()
