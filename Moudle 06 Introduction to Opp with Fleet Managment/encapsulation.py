#encapsultion mean -> hide details
#access modifier : public, protected, private

class Bank:
    def __init__(self,Holder_Name, Initial_deposite) -> None:
        self.holder_name = Holder_Name #public
        self._branch = "Mirpur 11" #protected
        self.__Balance = Initial_deposite #private

    def deposite(self,amount):
        self.__Balance += amount
    
    def get_balance(self):
        return self.__Balance
    
    def withdraw(self,amount):
        if amount <= self.__Balance:
            self.__Balance -= amount
            return amount
        else :
            return 'Insufficient funds'
    
rafsan = Bank('Choto vai ',100)

#acces public attribute:
print(rafsan.holder_name)
rafsan.holder_name= 'Meraz'
print(rafsan.holder_name)

# Accessing private attribute indirectly using a method
rafsan.deposite(20000)
print(rafsan.get_balance())

# Attempting to access protected attribute directly
print(rafsan._branch)

# Attempting to access private attribute directly (not recommended)
print(rafsan._Bank__Balance)  # Uncommenting this will print 50000


# Withdrawing money
print(rafsan.withdraw(20000))  # Output: 20000
print(rafsan.get_balance())  # Output: 30000