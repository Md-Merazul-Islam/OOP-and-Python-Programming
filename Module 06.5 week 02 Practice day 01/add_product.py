# class Product:
#     def __init__(self,Name,description, price,category) -> None:
#         self.name = Name
#         self.description =description
#         self.price =price
#         self.category = category
#     def display_list(self) -> str:
#         return f'Name : {self.name} , description : {self.description} , price : {self.price} catafory : {self.price}'


# class Shop :
        
#     def __init__(self) -> None:
#         self.my_list =[]
        
#     def add_product(self,product):
#         self.my_list.append(product)
        
#     def display_products(self):
#         for product in self.my_list:
#             print(product.display_list())
            

# Product1 = Product("Laptop","8GB Ram",20000,"first")
# my_shop = Shop()
# my_shop.add_product(Product1)
# my_shop.display_products()



class Product:
    def __init__(self,name,price) -> None:
        self.name =name
        self.price =price

class Shop:
    def __init__(self) -> None:
        self.mylist= []
        
    def add_product(self,products):
        self.mylist.append(products)

text = Shop()
text2 = Product("am",388)
text3= Product("jam",234)
text.add_product(text2)
text.add_product(text3)

for item in text.mylist:
    print(f'Name : {item.name} , price :${item.price}')
        