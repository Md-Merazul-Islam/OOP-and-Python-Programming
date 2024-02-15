# inheritance use kora hoy  jkhn parent class er boisito mil thake ba parent class ke access kore take poriborton ba prosarito korte cay tkhn.inheritance allow kore overridde korte 


# but composition er khetre amra seita class use korte pari ja amra chage ba kono poriboston add korte pari na. eivabe jkhn kono chanage kora chara class ta use kori tkhn amra composition use korte pari .

#inheritance :

class Animal:
    def __init__(self,name ) -> None:
        self.name = name 
        
    def sound (self):
        pass
class Dog(Animal):
    def sound(self):
        return "dogiii"
        # return super().sound() 
class Cat(Animal):
    def sound(self):
        # return super().sound()
        return "Cat"
dog = Dog("s")
print(dog.sound())

print(Cat("").sound())





# composition:
class Engine():
    def star(self):
        return f'Engine start'
class Glass:
    def glass(self):
        return f'Glass borken'

class Car:
    def __init__(self) -> None:
        self.engine = Engine()
        self.glass = Glass()
    
    def st(self):
        return self.engine.star()
    def gl (self):
        return self.glass.glass()
    
print(Car().gl())
print(Car().st())