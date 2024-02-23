import random
from datetime import datetime
from abc import ABC, abstractmethod


class Account(ABC):
    accounts = []

    def __init__(self, name, email, address, type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.type = type
        self.account_number = self.generate_random_account_number()
        self.balance = 0
        self.loan_count = 0
        self.transfer_history = []
        self.total_bank_balance = 0
        self.bankrupt = False
        self.loan_permission = True
        self.transfer_permission = True
        Account.accounts.append(self)

    def generate_random_account_number(self):
        return "".join(str(random.randint(0, 9))for i in range(2))


class User(Account):
    def __init__(self, name, email, address, type) -> None:
        super().__init__(name, email, address, type)

    def generate_random_account_number(self):
        return "".join(str(random.randint(0, 9))for i in range(2))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.total_bank_balance += amount
            self.transfer_history.append(
                ("Deposit", amount, self.account_number, datetime.now()))
            print(
                f'\n\t{amount} Tk successfully deposited. Now your new balance is {self.balance} Tk')
        else:
            print('\n\tInvalid deposit amount!')

    def withdraw(self, amount):
        if not self.bankrupt:
            if amount > 0:
                if self.balance >= amount:
                    self.balance -= amount
                    self.total_bank_balance -= amount
                    self.transfer_history.append(
                        ("Withdrawal", amount, self.account_number, datetime.now()))
                    print(
                        f'\n\t{amount} Tk successfully withdrawn. Now your available balance is {self.balance} Tk')
                else:
                    print('\n\tInsufficient balance!')
            else:
                print('\n\tInvalid withdrawal amount!')
        else:
            print('\n\tBank is Duoliya!')

    def available_balance(self):
        print(f'\n\tYour available balance is {self.balance} Tk')

    def transfer_balance(self, account_no, amount):
        if self.transfer_permission:
            if amount > 0:
                if self.balance >= amount:
                    receiver = None
                    for acc in Account.accounts:
                        if isinstance(acc, User) and acc.account_number == account_no:
                            receiver = acc
                            break
                    if receiver:
                        receiver.deposit(amount)
                        self.balance -= amount
                        self.transfer_history.append(
                            ("Transfer", amount, receiver.account_number, datetime.now()))
                        print(
                            f'\n\t{amount} Tk transferred from account {self.account_number} to account {receiver.account_number} successfully')
                    else:
                        print('\n\treceiver account not found!')
                else:
                    print('\n\tInsufficient balance!')
            else:
                print('\n\tInvalid transfer amount!')
        else:
            print('\n\tTransfer system is disabled!')

    def display_transfer_history(self):
        print('*******************************************Transfer history***********************************************')

        print(f"\tTransfer Type  \t\t Amount    \t  Account No \t\t\tDate Time ")
        print('----------------------------------------------------------------------------------------------------------')
        for tr in self.transfer_history:
            print(f"   \t{tr[0]} \t\t {tr[1]} Tk \t     {tr[2]} \t\t {tr[3]}")

    def take_loan(self, amount):
        if self.loan_permission:
            if self.loan_count < 2:
                self.balance += amount
                self.loan_count += 1
                self.total_bank_balance -= amount
                print(
                    f'\n\tLoan of {amount} Tk successfully taken. New balance is {self.balance} Tk')
            else:
                print('\n\tMaximum number of loans already taken!')
        else:
            print('\n\tLoan system is disabled by admin!')


# Example usage:
user1 = User("Meraz", "meraz@gmail.com", "Dhaka", "Savings")
user2 = User("Rakib", "rakib@gmail.com", "Gazipur", "Current")

user1.deposit(1000)
user1.withdraw(500)
user1.transfer_balance(user2.account_number, 200)
user1.available_balance()
user1.display_transfer_history()
user1.take_loan(300)


# Admin
class Admin(User):
    def __init__(self, name, email, address, type) -> None:
        super().__init__(name, email, address, type)

    def create_account():
        pass

    def delete_any_user(self, account_num):
        for acc in self.accounts:
            if acc.account_number == account_num:
                self.accounts.remove(acc)
                print(f'\n\t Successfully delete user.')
                return
        print(f'User account not found! ')

    def see_all_user_list(self):
        print('*******************************************Transfer history***********************************************')
        print(f"\tUser Name  \t\t Email     \t  Address \t\t\tAccount Type ")
        print('----------------------------------------------------------------------------------------------------------')
        for tr in self.self.accounts:
            print(f"   \t{tr[0]} \t\t {tr[1]} Tk \t     {tr[2]} \t\t {tr[3]}")

    def check_total_available_balance(self):
        print(
            f'\n\tBank total available balance is : {self.total_bank_balance} Tk')

    def show_total_loan(self):
        print(f'\n\tTotal loan is : {self.take_loan} Tk')

    def permisson_loand_on_off(self, isloan):
        if isloan == False:
            self.loan_permission = False
            print(f'\n\tSuccessfully,  loan feature of the bank off.')
        else:
            self.loan_permission = True

    def bankrupt_on_off(self, isbank_deoliya):
        if isbank_deoliya== True:
            self.bankrupt= True
            print(f'\n\tBank is deouliya. Manager Tk niya polaiche.')
        else:
            self.bankrupt = False

    def transfer_permission_on_off(self, transfer_per):
        if  transfer_per == False:
            self.transfer_permission = False
            print(f'\n\tSuccessfully, Transfer permisson off.')
        else:
            self.transfer_permission = True



