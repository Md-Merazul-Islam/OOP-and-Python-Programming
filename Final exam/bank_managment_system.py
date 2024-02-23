from abc import ABC, abstractmethod
import random
from datetime import datetime


class Account(ABC):
    accounts = []

    def __init__(self, name, email, address, type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.type = type
        self.account_number = self.ganarate_random_account_number()
        self.balance = 0
        self.bankrupt = False
        self.transfer_permisson = True
        self.loan_count = 0
        self.transfer_history = []
        self.loan_permisson = True
        self.net_load = 0
        Account.accounts.append(self)

    def ganarate_random_account_number(self):
        return "".join(str(random.randint(0, 9))for i in range(2))

class User(Account):
    def __init__(self, name, email, address, type) -> None:
        super().__init__(name, email, address, type)

    def ganarate_random_account_number(self):
        return "".join(str(random.randint(0, 9))for i in range(2))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transfer_history.append(("Deposit", amount, datetime.now()))
            print(
                f'{amount} Tk successfully deposit. Now you new balacne {self.balance} Tk')
        else:
            print(f'You have not enought money!')

    def withdraw(self, amount):
        if self.bankrupt == False:
            if amount >0:
                if self.balance >= amount:
                    self.balance -= amount
                    self.transfer_history.append(("Withdrawa", amount, datetime.now()))
                    print(f'{amount} tk withdraw successfull. Now you availbe balance {self.balance}')
                else:
                    print(f'You balance not enought!')
            else:
                print('Invalid withdraw!')
        else:
            print(f'*****SORRY,Bank has been bankrupt.*****')

    def available_balance(self):
        print(f'Hey, you available balance is {self.balance}')

    def transfer_balance(self, account_no, amount):
        if self.transfer_permisson == True:
            if amount > 0:
                if self.balance >= amount:
                    recipient = None
                    for user in Account.accounts:
                        if isinstance(user, User) and user.account_number == account_no:
                            recipient = user
                            break
                    if recipient:
                        recipient.deposit(amount)
                        self.balance -= amount
                        self.transfer_history.append(
                            "Transfer", amount, datetime.now())
                        print(
                            f'{amount} tk transfer from {self.account_number} account to {user.account_number}   successfuly. ')
                    else:
                        print(f'User not found!')
                else:
                    print('Not enought money!')
            else:
                print("Invalid amount!")
        else:
            print("Admin break the tansfer system!")
            
    def display_transfer_histroy(self):
        print('*********************************Transfer history**********************************')
        
        print(f" \tTransfer Type  \t\t Amount    \t \t\t Date ")
        print('-----------------------------------------------------------------------------------')
        for tr in self.transfer_history:
            print(f" \t{tr[0]} \t\t  {tr[1]} Tk \t\t {tr[2]}")

    def take_loan(self, amount):
        if self.loan_permisson == True:
            if self.loan_count <= 2:
                self.balance += amount
                self.net_load += amount
                print(f'Load {amount} tk successfully. New balance {self.balance}')
            else:
                print("Loan limit finished!")
        else:
            print("Admin off loan system!")

# Example usage:
user1 = User("John Doe", "john@example.com", "123 Main St", "Savings")
user2 = User("Jane Smith", "jane@example.com", "456 Elm St", "Current")

user1.deposit(1000)
user1.withdraw(500)
user1.transfer_balance(user2.account_number, 200)
user1.available_balance()
user1.display_transfer_histroy()
user1.take_loan(300)
