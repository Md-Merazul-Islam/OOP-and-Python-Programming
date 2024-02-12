class Product:
    def __init__(self,Name,description, price,category) -> None:
        self.name = Name
        self.description =description
        self.price =price
        self.category = category
        
    def __repr__(self) -> str:
        return f'Name : {self.name} , description : {self.description} , price : {self.price} catafory : {self.price}'


class Shop :
    def __init__(self,name,location,address,contact) -> None:
        self.name =name
        self.location = location
        self.address = address
        self.contact = contact
    
    def __repr__(self) -> str:
        return f'Name : {self.name} , Location : { self.location} address : {self.address} contact : {self.contact}'


my_product = Product("name","This is am ",100,2)
print(my_product)

my_shop = Shop("Vai vai telecom","Dhaladia","Gazipur","01404040494")
print(my_shop)