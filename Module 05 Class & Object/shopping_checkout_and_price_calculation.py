class shopping:
    def __init__ (self, name):
        self.name = name
        self.cart=[]
        
    def add_cart(self,item,price,quantity):
        product_list = {'Item name' : item, 'Price' : price, 'Quantity': quantity}
        self.cart.append(product_list)
    
    def checkout(self,amount):
        total=0
        for item in self.cart:
            total += (item['Price'] *item['Quantity'])
        print('Total price ',total)
        if amount < total:
            need = total - amount
            print(f'give me more {total-amount} tk plz')
        elif(amount> total):
            print(f'You will back {amount- total} tk')
        else:
            print("ok , successfull purchase. Thakyou")

bag = shopping('Family shope')
bag.add_cart('alu',50,6)
bag.add_cart('potol',4,3)
bag.add_cart('rice',23,55)
print(bag.cart)
bag.checkout(500)