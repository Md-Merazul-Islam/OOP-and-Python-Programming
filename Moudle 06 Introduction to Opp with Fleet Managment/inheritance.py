class Gadget:
    def __init__(self,brand,price,color) -> None:
        self.brand =brand
        self.price = price
        self.color = color
    
    def run(self):
        return f'Running laptop : {self.brand}'
    
    
class leptop(Gadget):
    def __init__(self,brand,price,color,storage,warenty) -> None:
         self.storage = storage
         self.wanrenty = warenty
         super().__init__(brand,price,color)
         
    def coding (self):
        return f'Learn python and practice'
    def __repr__(self) -> str:
        return f'Leptop : {self.brand} price : {self.price} color : {self.color} storage :{self.storage} warenty :{self.wanrenty}'
    
class Mobile(Gadget) :
    def __init__(self,brand,price,color,dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand,price,color)
        
    def phone_call(self,number,text):
        return f'{text} from {number}'
    def __repr__(self) -> str:
        return f'phone brand  : {self.brand} price: {self.price} Text: {self.dual_sim}'

    
    
class camera:
    def __init__(self,pixel) -> None:
        self.pixel =pixel
    
    def chg_len(self):
        pass
    
        
        
        
my_phone= Mobile ('Vivo',45080,"Blue",True)
print(my_phone)
my_leptop = leptop('Hp',100000,'Silver','1000GB','2 years')
print(my_leptop)


class MyClass:
    def my_function(self, *args, **kwargs):
        tl_sum = sum(args)
        tl_multi = 1
        for value in kwargs.values():
            tl_multi *= value
        return tl_sum, tl_multi

obj = MyClass()
addition, multiplication = obj.my_function(1, 2, 3, factor1=4, factor2=5)
print("Addition :", addition)
print("Multiplication :", multiplication)
