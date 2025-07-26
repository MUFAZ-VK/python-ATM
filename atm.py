# @MUFAZ-VK  | PYTHON ATM

class BankAccount:
    def __init__(self, name, acc_no):
        self.name = name
        self.acc_no = acc_no
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited Successfully")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not Enough Balance!")
        else:
            self.balance -= amount
            print("Amount Withdrawed")

    def view_balance(self):
        print(f"Balance is: {self.balance}")


# 🌟 Main Program
name = input("Enter the Account Holder Name: ")
acc_no = input("Enter the Account Number: ")

acc = BankAccount(name, acc_no)

print("ACCOUNT DETAILS")
print("---------------")
print(f"Account Holder: {acc.name}")
print(f"Account Number: {acc.acc_no}")

while True:
    print("\n1. Deposit Money")
    print("2. Withdraw Money")
    print("3. View Balance")
    print("4. Exit")

    choice = int(input("\nEnter the Choice: "))

    if choice == 1:
        amount = int(input("Enter the Amount to Deposit: "))
        acc.deposit(amount)

    elif choice == 2:
        amount = int(input("Enter the Amount to Withdraw: "))
        acc.withdraw(amount)

    elif choice == 3:
        acc.view_balance()

    elif choice == 4:
        print("Exiting!")
        break

    else:
        print("Invalid Choice! Please try again.")
