class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
        else:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")

    def account_info(self):
        print(f"Account holder: {self.name}")
        print(f"Balance: ₹{self.balance}")


name = input("Enter your name: ")
balance = int(input("Enter initial balance: "))

account = Bank(name, balance)

choice = input("Do you want to deposit or withdraw? ").lower()

if choice == "deposit":
    amount = int(input("How much do you want to deposit: "))
    account.deposit(amount)

elif choice == "withdraw":
    amount = int(input("How much do you want to withdraw: "))
    account.withdraw(amount)

else:
    print("Invalid choice.")

account.check_balance()