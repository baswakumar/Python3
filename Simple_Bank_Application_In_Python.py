'''WAPP to develop a simple Bank Application using the concepts to local, Static and Instance variables'''

import sys
class Bank:
    bankname="Bank Of India"
    def __init__(self,balance=0.0):
        self.balance = balance
    
    def withdraw(self,amount):
        if(self.balance < amount):
            print("Insufficient Balance")
            sys.exit(0)
        self.balance = self.balance - amount
        print("\n Current Balance after withdraw: ",self.balance)

    def deposit(self,amount):
        self.balance = self.balance +amount
        print("\n Current Balance after withdraw: ",self.balance)

bx = Bank()
print("Welcome to ",Bank.bankname)
while True:
    option = input("\nEnter -d for Deposit\nEnter -w for Withdraw\nEnter -e for Exit\n").lower()
    if option == 'd':
        amount = float(input("\nEnter the amount to be deposited\n"))
        bx.deposit(amount)

    elif option == 'w':
        amount = float(input("\nEnter the amount to be withdrawn\n"))
        if (amount < 100 or amount % 10 !=0):
            print("Please enter in the multiples of 100")
        else:
            bx.withdraw(amount)

    elif option == 'e':
        sys.exit(0)
    
    else:
        print("\nPlease enter a valid input")
