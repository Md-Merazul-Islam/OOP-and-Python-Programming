
class Bank:
    def __init__(self , Balance):
        self.balance = Balance
        self.min_withdraw= 100
        self.max_withdraw = 1000000
        
    def get_balance(self,amount):
        return self.balance

    def deposite(self,amount):
        if(amount >0):
            self.balance+=amount
            print(f'your {amount} tk is deposite successfull!. Now your balance is {self.balance}')
            print("Thankyou")
        else:
            print("plz input valid amount ")
    
    def withdraw(self, amount):
        if self.min_withdraw >amount:
            print(f'{amount} this amount is very poor , minimum deposite allowed {self.min_withdraw} tK')
        elif self.max_withdraw < amount:
            print(f'{amount} this amount is very high , maximum deposite allowed {self.max_withdraw} tK')
        else :
            self.balance -= amount
            print(f'your {amount} tk is withdraw successfull!. Now your balance is {self.balance}')
            print("Thankyou")

balance = int(input("How much money have you account ? : "))
test = int (input("What you want ? deposite or withdraw . if deposite, plz enter the digit 1 otherwise 2 :" ))
text = Bank(balance)

if(test==1):
    amount_of = int(input("How much money do you want deposite :"))
    text.deposite(amount_of)
else :
    amount_of = int(input("How much money do you want withdraw :"))
    text.withdraw(amount_of)
    
    


    