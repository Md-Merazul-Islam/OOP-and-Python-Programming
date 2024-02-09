# class shopping:
#     def __init__(self, name):
#         self.name = name
#         self.cart = []

#     def add_cart(self, item, price, quantity):
#         product_list = {'Item name': item,
#                         'Price': price,
#                         'Quantity': quantity
#                         }
#         self.cart.append(product_list)

#     def checkout(self, amount):
#         total = 0
#         for item in self.cart:
#             total += (item['Price'] * item['Quantity'])
#         print('Total price ', total)
#         if amount < total:
#             print(f'give me more {total-amount} tk plz')
#         elif (amount > total):
#             print(f'You will back {amount- total} tk')
#         else:
#             print("ok , successfull purchase. Thakyou")


# bag = shopping('Family shope')
# bag.add_cart('alu', 50, 6)
# bag.add_cart('potol', 4, 3)
# bag.add_cart('rice', 23, 55)
# print(bag.cart)
# bag.checkout(500)


class shoping:
    def __init__(self,name):
        self.nam= name
        self.cart = []
    def add_cart(self,item,price,quantity):
        product_list = {
            "Item": item,
            "Price":price,
            "Quantity":quantity
        }
        self.cart.append(product_list)
        
    def check_out (self,amount):
        total_cost = 0
        for item in self.cart:
            total_cost+= (item['Price'] * item ['Quantity'])
        if( total_cost < amount):
            print(f'Your owe me {abs(amount-total_cost)} Tk')
        elif (total_cost> amount):
            print(f'You will back {abs( total_cost-amount)} TK')
        else :
            print("Successfuly purcheas completer.Thankyou")
        
t =int(input("How many item do you want buy : "))
toli = shoping("from family shop")
for i in range(t):
    pr_name = str(input("Enter you product name : "))
    price_ = int(input("Enter the price of this product : "))
    quntity_= int(input("Enter the quantity : "))
    toli.add_cart(pr_name,price_,quntity_)

print("this is you list :" ,toli.cart)

amount_ = int(input("Now give me money : "))
toli.check_out(amount_)


d