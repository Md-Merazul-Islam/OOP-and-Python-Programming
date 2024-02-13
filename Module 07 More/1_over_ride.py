class Person:
    def __init__(self,name,age,height,weight) -> None:
        self.name = name 
        self.age= age
        self.height = height
        self.weight = weight
    
    def eat(self):
        print("I eat ")
    

class Cricketer(Person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team  = team
        super().__init__(name, age, height, weight)
        
        
    def eat(self):
        print("Cricketer eat gash")
        
    def __add__(self,other):
        return self.age + other.age
    def __mod__(self,other):
        return self.height % other.height
    
        

meraz = Cricketer("Meraz",21,70,67,"DHS")
sakib = Cricketer("sakib",22,55,76,"RHS")
meraz.eat()

print(meraz + sakib)
print(meraz % sakib)