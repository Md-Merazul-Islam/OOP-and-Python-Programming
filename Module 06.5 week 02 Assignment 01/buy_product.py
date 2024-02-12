class Product :
    def __init__(self,name,price) -> None:
        self.name = name
        self.price =price

class Shop :
    def __init__(self) -> None:
        self.product_list = ['Apple','Mango','Banana','Lichu','Jackfriuts']
    
    def buy_product(self,item):
        for product in self.product_list:
            if(product== item):
                return f'Successfully buy {item}'
        
        return f'Sorry this {item} is not avilable'
    
shop =Shop()
text = shop.buy_product('Apple')
print(text)    
    
        