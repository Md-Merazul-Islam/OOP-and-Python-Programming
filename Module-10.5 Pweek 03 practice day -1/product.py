class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    @staticmethod
    def buy_product(shopping, product_id, buyer_balance):
        for product in shopping.products_list:
            if product['id'] == int(product_id):
                if product['quantity'] > 0:
                    if buyer_balance >= product['price']:
                        product['quantity'] -= 1
                        balance = buyer_balance - product['price']
                        print(f'You will get back {balance} Tk.')
                        print('Successfully bought.')
                        return product['price']
                    else:
                        print("You do not have enough balance.")
                        return 0
                else:
                    print("This item is already finished")
                    return 0
        else:
            print('Item not found')
            return 0