class vichle:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        
class bus(vichle):
    def __init__(self, name, price, seat) -> None:
        self.seat = seat
        super().__init__(name, price)  
    def __repr__(self) -> str:
        return f'Bus name : {self.name} price : {self.price} seat : {self.seat}'
        
class truck(vichle):
    def __init__(self, name, price, load) -> None:
        self.load = load
        super().__init__(name, price)  
    def __repr__(self) -> str:
        return f'Truck Name : {self.name} price : {self.price} load : {self.load}'

class pickuptrack(truck):
    def __init__(self, name, price, load) -> None:
        super().__init__(name, price, load)
    def __repr__(self) -> str:
        return f'pickup truck : name {self.name} price {self.price} Load {self.load}'
    
class AcBus(bus):
    def __init__(self, name, price, seat, tamperature) -> None:
        self.temparature = tamperature
        super().__init__(name, price, seat)  
        
    def __repr__(self) -> str:
        return f'AcBus : Name {self.name} price {self.price} seat {self.seat} temperature {self.temparature}'

acbus = AcBus("shonar bangla", 408, 45, 16)
print(acbus)
