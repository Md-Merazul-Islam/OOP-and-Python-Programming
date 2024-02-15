

class Animal:
    def __init__(self, name) -> None:
        self.name = name
        pass

    @classmethod
    def get_age(self, age):
        return 18 < age
    
    @staticmethod
    def add(x,y):
        return x+y

print(Animal.get_age(10))
ans = Animal("her")
print(ans.add(2,3))
