"""
Encapsulation allows for the hiding of the internal state of an object and only exposing the necessary functionalities to interact with that object. This helps in achieving data abstraction, where the implementation details are hidden from the outside world, and only the interface to interact with the object is exposed.

The three main access modifiers are: public, protected, and private.

1. **Public**: Public members are accessible from outside the class. They can be accessed by any code that has access to the object.
2. **Protected**: Protected members are accessible within the class itself and by its subclasses. They are not directly accessible from outside the class or its subclasses.
3. **Private**: Private members are only accessible within the class itself. They cannot be accessed directly from outside the class, not even by subclasses.

"""


class Bank:
    def __init__(self, Holder_Name, Initial_deposite) -> None:
        self.holder_name = Holder_Name  # public attribute
        self._branch = "Mirpur 11"  # protected attribute
        self.__Balance = Initial_deposite  # private attribute

    def deposite(self, amount):
        self.__Balance += amount
    
    def get_balance(self):
        return self.__Balance
    
    def withdraw(self, amount):
        if amount <= self.__Balance:
            self.__Balance -= amount
            return amount
        else:
            return 'Insufficient funds'

# Creating an instance of the Bank class
rafsan = Bank('Choto vai ', 100)

# Access public attribute
print(rafsan.holder_name)  # Output: Choto vai
rafsan.holder_name = 'Meraz'
print(rafsan.holder_name)  # Output: Meraz

# Accessing private attribute indirectly using a method
rafsan.deposite(20000)
print(rafsan.get_balance())  # Output: 20100 (initial deposit 100 + deposited 20000)

# Attempting to access protected attribute directly
print(rafsan._branch)  # Output: Mirpur 11

# Attempting to access private attribute directly (not recommended)
print(rafsan._Bank__Balance)  # Uncommenting this will print 20100

# Withdrawing money
print(rafsan.withdraw(20000))  # Output: 20000
print(rafsan.get_balance())  # Output: 100 (20100 - withdrawn 20000)


