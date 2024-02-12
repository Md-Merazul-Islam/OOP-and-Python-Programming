from math import pi
class Shape:
    def __init__(self, name) -> None:
        self.name= name


class Ractangle(Shape):
    def __init__(self, name, w, h) -> None:
        self.w = w
        self.h = h
        super().__init__(name)
    def area (self):
        return f'The ractangle area is : {self.w*self.h}'
    
class Circle (Shape):
    def __init__(self, name,radius) -> None:
        self.radius= radius
        super().__init__(name)
    def area(self):
        return f'The circle area is : {pi *self.radius**2}'

rec = Ractangle("rac",20,10)
print(rec.area())

chp = Circle("cl",5)
print(chp.area())