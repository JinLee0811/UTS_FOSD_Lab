# # class Account:
# #     def __init__(self):
# #         self.balance = 0.0
# #         # self.type = ""


# # class Bank(Account):
# #     def __init__(self, balance):
# #         print("Amount to deposit $", end="")
# #         amount = float(input())
# #         print("Amount ${0} deposited".format(amount))
# #         self.balance += amount
# #         print("Balance is ${0}".format(self.balance))

# #         print("Amount to withdraw $", end="")
# #         amount = float(input())
# #         print("Amount ${0} withdrawn".format(amount))
# #         self.balance -= amount
# #         print("Balance is ${0}".format(self.balance))


# # class Customer:
# #     def __init__(self):
# #         self.name = ""
# #         self.accounts = []


# # class Manager:
# #     def __init__(self):
# #         self.name = ""


# # Bank()


# # 이름과 계좌 등록하기
# # 돈을 넣기전에 신원확인 (이름, 계좌번호 받기)
# # 어카운트들 배열에 이름과 계좌번호가 있는 지 확인
# # 이름 계좌번호 화면에 띄우고 해당 계좌로 얼마 입금 할건지 deposit amount
# # 입금 후 잔액 확인
# # 종료할건지 or 출금 할건지 선택게하기
# # 출금 선택 시 얼마 출금 할건지 withdraw amount
# # 출금 후 잔액 확인
# # 종료 선택 시 종료


# customerList = []


# # 이름과 계좌 등록하기
# class Account:
#     def __init__(self, name, accountNumber, balance):
#         self.name = name
#         self.accountNumber = accountNumber
#         self.balance = balance
#         customer = [self.name, self.accountNumber, self.balance]
#         customerList.append(customer)
#         print(
#             f"Hello? Mr/Ms {self.name}, your account Number is [ {self.accountNumber} ]"
#         )


# class Customer:
#     def __init__(self, name="", accountNumber="", balance=0.0):
#         self.name = name
#         self.accountNumber = accountNumber
#         self.balance = balance

#     def deposit(self):
#         print("Deposit")
#         deposit_amount = float(input("Deposit amount: "))
#         self.balance += deposit_amount

#     def withdraw(self):
#         print("Withdraw")
#         withdraw_amount = float(input("Withdraw amount: "))
#         self.balance -= withdraw_amount

#     def checkBalance(self):
#         print(f"Your balance is {self.balance}")


# # 객체 생성 및 테스트
# customer = Account("John Doe", "123456789", 0)
# # customer1 = Customer("John Doe", "123456789", 0)
# # customer1.deposit()
# # customer1.withdraw()
# # customer1.checkBalance()

# print(customerList)
