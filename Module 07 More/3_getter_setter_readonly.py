# read only --> you can not set the value. value can not be changed
# getter --> get a value of a property through a method. Most of the time, you will get the value of a private attribute.
# setter --> set a value of a property through a method. Most of the time, you will set the value of a private property.


class User:
    def __init__(self, name, age, money) -> None:
        self.name = name  # public
        self._age = age  # protected
        self.__money = money  # private

    # if we not use getter it will be randomly setter
    @property
    def age(self):
        return self._age
    #getter
    @property
    def balance(self):
        return self.__money
    
    #setter 
    @balance.setter
    def balance(self,amount):
        if amount <0:
            return f'This amount is negative '
        else :
            self.__money += amount


text = User("sakib", 67, 209)
# print(text.age()) #without property use
print(text.age)  # after use porperty

print(text.balance)

text.balance = 20000
print(text.balance)