# class to handle deposite and withdrawl in a bank

import sys


class Bank(object):
    # to initialize name and balance instance variables.
    def __init__(self, name = '', balance = 0.0):
        self.name = name
        self.balance = balance

    # add deposite amount to balance

    def deposite(self, amount):
        self.balance += amount
        return self.balance

    # to deduct withdrawal amount from balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            print('Balance is less. Withdrawl Not possible. ')
            return self.balance


# using the Bank Class

name = input("Enter name: ")
b = Bank(name)

# Repeat continuously until it finds 'e' or 'E'

while True:
    print('\n d - Deposite \n w - Withdraw \n e - Exit')
    choice = input('Enter Your Choice: \n')
    if choice == 'e' or choice == 'E':
        sys.exit()
    amount = int(input('Enter withdraw / deposite amount: '))

    if choice == 'd' or choice == 'D':
        print('Balance after deposite: ',b.deposite(amount))
    elif choice == 'w' or choice == 'W':
        print('Balance after withdraw: ',b.withdraw(amount))
