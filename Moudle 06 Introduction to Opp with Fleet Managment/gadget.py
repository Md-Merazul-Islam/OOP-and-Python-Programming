class Laptop:
    def __init__(self,brand,price, color, memory) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory =memory
        
    def run(self):
        return f'Running laptop : {self.brand}'
    def coding(self):
        return f'Learing python and practicing'
    
class phone:
    def __init__(self,brand,price,color,sim) -> None:
        self.brand = brand
        self.price = price
        self.price= price
        self.sim = sim
        
    def run(self):
        return f'Running mobile : {self.brand}'
    def phone_call(self,number, sms):
        return f'Sending msg {sms} from {number}'
    
class Camera :
    def __init__(self,brand,price,color,lens) -> None:
         self.brand = brand
         self.price = price
         self.color = color
         self.lens = lens
         
    def run (self):
        return f'camera st'
    def chg_lens(self):
        return 'changed successed'
