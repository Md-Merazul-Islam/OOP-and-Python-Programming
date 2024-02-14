class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

class Shop:
    def __init__(self) -> None:
        self.mylist = []
        
    def add_product(self, product):
        self.mylist.append(product)
        
class DiscountedProduct(Product):
    def __init__(self, name, price, discount) -> None:
        super().__init__(name, price)
        self.discount = discount
        
    def get_discounted_price(self):
        return self.price * (1 - self.discount)
    
text = Shop()
text2 = Product("am", 388)
text3 = Product("jam", 234)
text.add_product(text2)
text.add_product(text3)

product_ans = DiscountedProduct("alu", 1000, 0.1)  # Discounted price with 10% discount
text.add_product(product_ans)

for item in text.mylist:
    if isinstance(item, DiscountedProduct):
        print(f'Name: {item.name}, Price: ${item.price}, Discount: {item.discount}, Discounted Price: ${item.get_discounted_price()}')
    else:
        print(f'Name: {item.name}, Price: ${item.price}')
