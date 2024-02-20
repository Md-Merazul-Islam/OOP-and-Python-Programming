class Shopping:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.products_list = []

    def add_user(self, email, password, user_type):
        for user in self.users:
            if user['email'] == email:
                print(f'This {email} already exists')
                return
        user = {'email': email, 'password': password, 'type': user_type}
        self.users.append(user)
        return user

    def add_product(self, product_id, name, price, quantity):
        product = {'id': product_id, 'name': name,
                   'price': price, 'quantity': quantity}
        self.products_list.append(product)

    def show_products_list(self):
        print("Products List : ")
        for prd in self.products_list:
            print(
                f"Id: {prd['id']}, Name: {prd['name']}, Price: {prd['price']}, Quantity: {prd['quantity']}")