from abc import ABC,abstractmethod
class Animal(ABC) :
    @abstractmethod
    def eat (sef):
        pass
    @abstractmethod
    def move (self):
        pass
    
class Monkey(Animal) :
    def __init__(self,name) -> None:
        self.name=name
        self.category = 'Monkey'
        super().__init__()
        pass
    
    def eat(sef):
        # return super().eat()
        print('This is eat fun')
    def move(self):
        # return super().move()
        print("this is move fun")
    
    
text = Monkey("Banor")
text.eat()
text.move()