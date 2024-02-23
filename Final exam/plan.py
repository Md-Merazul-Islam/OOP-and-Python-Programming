"""
account -> name, email, address, acountType 
------------------------------------------------------------------
                        user
-----------------------------------------------------------------
atribute -> balance =0, account num += len(user[])
method -> 
0.if bank deoliya then chek 
1.deposite (error handling)
2.withdraw, (error handleing) (if bank not deuliya)
3.available balance 
4.transfer history 
5.loan max 2 time (admin check )
6.transfer balanace account to account if this use is valid
------------------------------------------------------------------


--------------------------------------------------------
                        admin
--------------------------------------------------------
method->
1. create account
2.delete any user
3.see all user acount list
4.can chk total available balance 
5.total loan
6.can off loan future

"""


import random
from datetime import datetime


class Account:
    accounts = []
    total_bank_balance = 0
    total_loan = 0

    def __init__(self, name, email, address, account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = self.generate_random_account_number()
        self.balance = 0
        self.loan_count = 0
        self.loan_amount = 0
        self.transfer_history = []
        self.bankrupt = False
        self.loan_permission = True
        self.transfer_permission = True
        Account.accounts.append(self)

    def generate_random_account_number(self):
        return "".join(str(random.randint(0, 9)) for i in range(2))


class User(Account):
    def __init__(self, name, email, address, account_type) -> None:
        super().__init__(name, email, address, account_type)

    def take_loan(self, amount):
        if self.loan_permission:
            if self.loan_count <= 2:
                self.balance += amount
                self.loan_count += 1
                self.loan_amount += amount
                Account.total_loan += amount
                Account.total_bank_balance -= amount
                print(
                    f'\n\tLoan of {amount} Tk successfully taken. New balance is {self.balance} Tk')
            else:
                print('\n\tMaximum number of loans already taken!')
        else:
            print('\n\tLoan system is disabled by admin!')

    def display_loan_amount(self):
        print(f'\n\tYour total loan amount is {self.loan_amount} Tk')

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            Account.total_bank_balance += amount
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
                    Account.total_bank_balance -= amount
                    self.transfer_history.append(
                        ("Withdrawal", amount, self.account_number, datetime.now()))
                    print(
                        f'\n\t{amount} Tk successfully withdrawn. Now your available balance is {self.balance} Tk')
                else:
                    print('\n\tInsufficient balance!')
            else:
                print('\n\tInvalid withdrawal amount!')
        else:
            print('\n\tBank is bankrupt!')

    def available_balance(self):
        print(f'\n\tYour available balance is {self.balance} Tk')

    def transfer_balance(self, account_no, amount):
        if self.transfer_permission:
            if amount > 0:
                if self.balance >= amount:
                    receiver = next((acc for acc in Account.accounts if isinstance(
                        acc, User) and acc.account_number == account_no), None)
                    if receiver:
                        receiver.deposit(amount)
                        self.balance -= amount
                        self.transfer_history.append(
                            ("Transfer", amount, receiver.account_number, datetime.now()))
                        print(
                            f'\n\t{amount} Tk transferred from account {self.account_number} to account {receiver.account_number} successfully')
                    else:
                        print('\n\tReceiver account not found!')
                else:
                    print('\n\tInsufficient balance!')
            else:
                print('\n\tInvalid transfer amount!')
        else:
            print('\n\tTransfer system is disabled!')

    def display_transfer_history(self):
        print('*******************************************Transaction history***********************************************')
        print(f"\tTransaction Type  \t Amount    \t  Account No \t\t\tDate Time ")
        print('----------------------------------------------------------------------------------------------------------')
        for tr in self.transfer_history:
            print(
                f"   \t{tr[0]} \t\t {tr[1]} Tk \t\t\t     {tr[2]} \t\t {tr[3]}")


class Admin(Account):
    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address, "Admin")

    def show_total_loan(self):
        print(f'\n\tBank total loan is : {Account.total_loan} Tk')

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        print(
            f"Account created for {name} with email {email} and account number {user.account_number}")

    def delete_any_user(self, account_name):
        for acc in Account.accounts:
            if isinstance(acc, User) and acc.name == account_name:
                Account.accounts.remove(acc)
                print(f'\n\tSuccessfully deleted user.')
                return
        print(f'\n\tUser account not found!')

    def see_all_user_list(self):
        print('**************************************************User Account List****************************************************')
        print(f"\tUser Name \t\tEmail \t\tAddress \t\tAccount Type\t\tAccount Number ")
        print('-------------------------------------------------------------------------------------------------------------------------')
        for acc in Account.accounts:
            if isinstance(acc, User):
                print(
                    f'\t{acc.name} \t\t {acc.email} \t{acc.address} \t\t {acc.account_type}   \t\t\t {acc.account_number}')

    def check_total_available_balance(self):
        print(
            f'\n\tBank total available balance is : {Account.total_bank_balance} Tk')

    def permission_loan_on_off(self, is_loan):
        if not is_loan:
            for user in Account.accounts:
                if isinstance(user, User):
                    user.loan_permission = False
            print(f'\n\tLoan feature of the bank is now off.')
        else:
            for user in Account.accounts:
                if isinstance(user, User):
                    user.loan_permission = True
            print(f'\n\tLoan feature of the bank is now on.')

    def bankrupt_on_off(is_bankrupt):
        if is_bankrupt:
            for user in Account.accounts:
                if isinstance(user, User):
                    user.bankrupt = True
            print(f'\n\tBank is bankrupt. Manager ran away with the money.')
        else:
            for user in Account.accounts:
                if isinstance(user, User):
                    user.bankrupt = False
            print(f'\n\tBank is no longer bankrupt.')

    def transfer_permission_on_off(self, transfer_per):
        if not transfer_per:
            for user in Account.accounts:
                if isinstance(user, User):
                    user.transfer_permission = False
            print(f'\n\tTransfer permission is now off.')
        else:
            for user in Account.accounts:
                if isinstance(user, User):
                    user.transfer_permission = True
            print(f'\n\tTransfer permission is now on.')


admin = Admin("admin", "admin@gmail.com", "kasimpur")
user1 = User("rakib", "rakib@gmail.com", "rajbari", "user")
user2 = User("sakib", "sakib@gmail.com", "shegubbag", "user")

currentUser = None
while True:
    if currentUser is None:
        print(f'\n\t Please Register or Log in!')
        ch = input("\n\tAdmin or User? (ad/ur) : ").lower()
        if ch == 'ur':
            option = input("\n\tLog in or Register? (L/R)  :").lower()
            if option == 'r':
                name = input("\n\tName : ")
                email = input("\n\tEmail : ")
                address = input("\n\tAddress : ")
                account_type = input(
                    "\n\tAccount type: Savings or Current?  (sv/cr) : ")
                User(name, email, address, account_type)
                currentUser = User(name, email, address, account_type)
            elif option == 'l':
                name = input("\n\tName : ")
                email = input("\n\tEmail : ")
                ok = False
                for acc in Account.accounts:
                    if isinstance(acc, User) and acc.name == name and acc.email == email:
                        currentUser = acc
                        ok = True
                        break
                if not ok:
                    print('\n\tYour information is incorrect!')
            else:
                print("\n\tInvalid option!")

        elif ch == 'ad':
            name = input("\n\tAdmin name : ")
            password = input("\n\tAdmin password : ")
            if password == "123" and name == "admin":
                currentUser = admin
            else:
                print("\n\tCheck your password or name again!")
        else:
            print("\n\tInvalid option!")
    else:
        print(f'\n\tWelcome {currentUser.name}')
        if isinstance(currentUser, User):
            print('\n\t-----------User Menu-------------- ')
            print("\t1. Deposit ")
            print("\t2. Withdraw")
            print("\t3. Available Balance")
            print("\t4. Transaction history")
            print("\t5. Take Loan")
            print("\t6. Transfer balance to another account")
            print("\t7. My total loan")
            print("\t8. Logout")

            op = int(input("\n\tChoose an option : "))
            if op == 1:
                amount = int(input("\n\tEnter the amount to deposit : "))
                currentUser.deposit(amount)
            elif op == 2:
                amount = int(input("\n\tEnter the amount to withdraw : "))
                currentUser.withdraw(amount)
            elif op == 3:
                currentUser.available_balance()
            elif op == 4:
                currentUser.display_transfer_history()
            elif op == 5:
                amount = int(input("\n\tEnter the amount to loan : "))
                currentUser.take_loan(amount)
            elif op == 6:
                account_no = input(
                    "\n\tEnter the account number to transfer : ")
                amount = int(input("\n\tEnter the amount to transfer : "))
                currentUser.transfer_balance(account_no, amount)
            elif op == 7:
                currentUser.display_loan_amount()
            elif op == 8:
                currentUser = None
            else:
                print("\n\tInvalid option!")
        else:
            print('\n\t-----------Admin Menu-------------- ')
            print("\t1. Create account ")
            print("\t2. Delete user")
            print("\t3. See all user account list ")
            print("\t4. Available total balance")
            print("\t5. See total loan")
            print("\t6. Turn off loan feature")
            print("\t7. Turn off transfer feature")
            print("\t8. Bankrupt ")
            print("\t9. Logout")
            # admin = Admin("admin", "admin@gmail.com", "kasimpur")
            op = int(input("\n\tChoose an option : "))
            if op == 1:
                name = input("\n\tName : ")
                email = input("\n\tEmail : ")
                address = input("\n\tAddress : ")
                account_type = input(
                    "\n\tAccount type: User or Admin?  (user/admin) : ")
                currentUser.create_account(name, email, address, account_type)
            elif op == 2:
                name = input("\n\tEnter the account name to delete : ")
                currentUser.delete_any_user(name)
            elif op == 3:
                currentUser.see_all_user_list()
            elif op == 4:
                currentUser.check_total_available_balance()
            elif op == 5:
                currentUser.show_total_loan()

            elif op == 6:
                cmd = input(
                    "\n\tDo you want to turn off loan feature? (yes/no)  : ").lower()
                if cmd == "yes":
                    currentUser.permission_loan_on_off(False)
            elif op == 7:
                cmd = input(
                    "\n\tDo you want to turn off transfer feature? (yes/no)  : ").lower()
                if cmd == 'yes':
                    currentUser.transfer_permission_on_off(False)

            elif op == 8:
                cmd = input("\n\tManager Tk niya bagche ? (yes/no)  : ")
                if cmd == "yes":
                    Admin.bankrupt_on_off(True)
            elif op == 9:
                currentUser = None
            else:
                print("\nt\tInvlid option!")
