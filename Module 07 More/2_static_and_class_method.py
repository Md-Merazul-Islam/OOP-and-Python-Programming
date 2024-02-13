class Shoping:
    def __init__(self,name,location) -> None:
        self.name = name
        self.location = location
    def purchase(self,item,price,amount):
        remaining = amount - price
        print(f'After buy this {item} for price ${price} and remaning :{remaining }')
    @staticmethod
    def multiply(a,b):
        ans = a*b
        print(ans)
        
    @classmethod 
    def hudai_ghuri(self, item):
        print(f' And buy {item}')

        
        
        
jomuna  = Shoping("jumuna future park ","Dhaka")
jomuna.purchase("Mobile",20000,222)
jomuna.hudai_ghuri("sun glass")
jomuna.multiply(2,34)