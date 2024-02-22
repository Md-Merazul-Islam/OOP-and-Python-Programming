from abc import ABC, abstractmethod


class Account(ABC):
    accounts = []

    def __init__(self, name, aco_num, password, type) -> None:
        self.name = name
        self.aco_num = aco_num
        self.password = password
        self.balance = 0
        self.type = type
        Account.accounts.append(self)

    def changeInfo(self, name):
        self.name = name
        print(f'Name changed of {self.aco_num}')
        
    # Overloading of method
    def changeInfo(self, name, pas):
        self.name = name
        self.pas = pas
        print(f'Name and password are changed of : {self.aco_num}')

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f'{amount} Tk Deposite successfully.New balance {self.balance}')
        else:
            print("Not enought money!")
    @abstractmethod
    def showInfo(self):
        pass
    
class SavingAccount(Account):
    def __init__(self, name, aco_num, password,interestRate) -> None:
        super().__init__(name, aco_num, password, "saving")
        self.interestRate = interestRate
    
    def apply_interest(self):
        interest = self.balance * (self.interestRate/100)
        self.deposit(interest)
        print(f'After interest you balance is {self.balance}')
    
    def showInfo(self):
        print(f'Info of {self.type} account of {self.name}')
        print(f'Name : {self.name}')
        print(f'Account No : {self.aco_num}')
        print(f'Current balance : {self.balance}')
        
class SpecialAccount(Account):
    def __init__(self, name, aco_num, password, limit) -> None:
        super().__init__(name, aco_num, password, "special")
        self.limit = limit
        
    def withdraw(self,amount):
        if amount>0 and (self.balance - amount)>=-self.limit:
            self.balance -= amount
            print(f'Withdraw ${amount} is successfull. Now new balance ${self.balance}')
        else:
            print(f'Invalid withdraw. amount over limit.')
    def showInfo(self):
        print(f'Info of {self.type} account of {self.name}')
        print(f'Name : {self.name}')
        print(f'Account No : {self.aco_num}')
        print(f'Current balance : {self.balance}')
        
        
        
currentUser= None
while(True):
    if currentUser==None:
        print(f'No user logged in!')
        option = input("Register or Loging?  (R/L) : ")
        if option=='R':
            name = input("Name : ")
            acout_num = input("Acccount Number : ")
            password = input("Password : ")
            user_type = input("Special or Saving use ? (sp / sv) : ")
            if user_type =="sp":
                limit = int(input("How much your limit : "))
                user = SpecialAccount(name,acout_num,password,limit)
                currentUser= user
            elif user_type=="sv":
                iRate = int(input("How interestRate : "))
                user = SavingAccount(name,acout_num,password,iRate)
                currentUser = user
            else:
                print("Choice correct option!")
        elif option=='L':
            acout_num = input("Acccount Number : ")
            for account in Account.accounts:
                if acout_num == account.aco_num:
                    currentUser = account
                    break
        else :
            print("Choice correct option!")
    else:
        print(f'welcome {currentUser.name}')
        if currentUser=='saving':
            print('You are a saving user, Menu here: ')
            print("1 : ShowInfo")
            print("2 : Deposite")
            print("3 : withdraw")
            print("4 : Change Inforamtion")
            print("5 : Apply Interset")
            print("6 : Logout")
            opt = int(input("Chosse a option : "))
            if opt==1:
                currentUser.showInfo()
            elif opt==2:
                amount = int(input("How many money do you deposite  : "))
                currentUser.deposit(amount)
            elif opt==3:
                amount = int(input("How many money do you withdraw  : "))
                currentUser.withdraw(amount)
            elif opt==4:
                name = input("New name : ")
                currentUser.changeInfo(name)
            elif opt==5:
                currentUser.apply_interest()
            elif opt==6:
                currentUser = None
            else :
                print("Invalid option!")
        else :
            print('You are a special user, Menu here: ')
            print("1 : ShowInfo")
            print("2 : Deposite")
            print("3 : withdraw")
            print("4 : Change Inforamtion")
            print("5 : Logout")
            opt = int(input("Chosse a option : "))
            if opt==1:
                currentUser.showInfo()
            elif opt==2:
                amount = int(input("How many money do you deposite  : "))
                currentUser.deposit(amount)
            elif opt==3:
                amount = int(input("How many money do you withdraw  : "))
                currentUser.withdraw(amount)
            elif opt==4:
                name = input("New name : ")
                password = input("New Password : ")
                currentUser.changeInfo(name,password)
            elif opt==5:
                currentUser = None
            else :
                print("Invalid option!")
                
                