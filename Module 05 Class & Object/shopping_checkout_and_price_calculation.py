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
            print(f'Your will back money of {abs(amount-total_cost)} Tk')
        elif (total_cost> amount):
            print(f'Give me {abs( total_cost-amount)} TK')
        else :
            print("Successfuly purcheas completer.Thankyou")
            
    def remove_item(self,element):
        for item in self.cart:
            if item['Item']==element:
                self.cart.remove(item)
                print(f'{element} is removed successfully.')
                
                print(f'Now you cart is : {self.cart}')
                return
        print(f'{element} not fount !')
    
    
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

remove_el= str(input("Enter the name of the removal element : "))
toli.remove_item(remove_el)



