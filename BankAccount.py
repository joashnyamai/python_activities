#Python BankAccount with classes and objects
class BankAccount:
    def __init__(self, account_number, customer_name, initial_balance, date_of_opening):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = initial_balance
        self.date_of_opening = date_of_opening

    def deposit(self, amount):
        self.balance += amount
        return amount  
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"  
        else:
            self.balance -= amount
            return amount  

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: ${self.balance}")

account_number = input("Enter account number: ")
customer_name = input("Enter customer name: ")
initial_balance = float(input("Enter initial balance: "))
date_of_opening = input("Enter date of opening (YYYY-MM-DD): ")

account = BankAccount(account_number, customer_name, initial_balance, date_of_opening)

while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Show Customer Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        print(f"Depositing ${amount}:")
        print(f"Amount deposited: ${account.deposit(amount)}")

    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        print(f"Withdrawing ${amount}:")
        print(f"Amount withdrawn: ${account.withdraw(amount)}")

    elif choice == '3':
        account.check_balance()

    elif choice == '4':
        account.customer_details()

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")