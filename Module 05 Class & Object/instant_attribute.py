class shop:
    
    def __init__(self,buyer):
        self.cart=[]
        self.name = buyer
    def add_product (self,item):
        self.cart.append(item)

meraz = shop("couffee house ")
meraz.add_product("tea")
meraz.add_product("coufee")
meraz.add_product("Senterfoot")
print(meraz.cart)

rakib = shop("Sultan dain")
rakib.add_product("Kacchi")
rakib.add_product("biriyani")
rakib.add_product("khichuri")
print(rakib.cart)

antor = shop("shoping mall")
antor.add_product("Mobile")
antor.add_product("Eair phone")
antor.add_product("bike")
print(antor.cart)