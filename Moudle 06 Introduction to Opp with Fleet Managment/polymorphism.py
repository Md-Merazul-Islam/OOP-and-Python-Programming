class Animal:
    def __init__(self,name) -> None:
        self.name = name
    def make_sound(self):
        print("Animal making some sound")

class Cat(Animal) :
    def __init__(self, name) -> None:
        super().__init__(name)
        
    def make_sound(self):
        print("Cat : meow")

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print("Dog : geo geo")

class Chagol(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print("Chagol gas khay")

an = Animal("a")
# an.make_sound()

ct = Cat('a')
# ct.make_sound()

at = Dog('r')
# at.make_sound()

chg = Chagol("d")
# chg.make_sound()


Animals = [an,ct,at,chg]
for animal in Animals:
    animal.make_sound()