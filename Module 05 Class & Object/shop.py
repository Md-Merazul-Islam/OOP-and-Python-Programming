class shop:
    cart =[]
    def __init__(self,Buyer):
        self.buyer = Buyer
    
    def at_product(self, item ):
        self.cart.append(item)

meraz =  shop("meraz")
meraz.at_product('ajhsflk')
meraz.at_product('aasdf')
meraz.at_product('aasdfksadhvh')
print(shop.cart)

meraz =  shop("meraz")
meraz.at_product('ajhsflk')
meraz.at_product('aasdf')
meraz.at_product('aasdfksadhvh')
print(shop.cart)