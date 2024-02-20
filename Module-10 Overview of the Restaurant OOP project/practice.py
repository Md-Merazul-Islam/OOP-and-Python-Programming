class Restaurant:
    def __init__(self, name, location, opening_hours):
        self.name = name
        self.location = location
        self.opening_hours = opening_hours
        self.tables = []
        self.Menu = Menu()  # Corrected attribute name

    def add_table(self, table):
        self.tables.append(table)

    def remove_table(self, table):
        self.tables.remove(table)

    def add_staff(self, staff_member):
        self.tables.append(staff_member)

    def remove_staff(self, staff_member):
        self.tables.remove(staff_member)

    def __str__(self):
        return f"Restaurant: {self.name}\nLocation: {self.location}\nOpening Hours: {self.opening_hours}"

class Menu:
    def __init__(self):
        self.items = []
        self.categories = []
        self.prices = {}
        self.specials = []

    def add_item(self, item, category, price):  # Removed 'subcategory' parameter
        self.items.append(item)
        if category not in self.categories:
            self.categories.append(category)
        self.prices[item] = price

    def remove_item(self, item):
        self.items.remove(item)
        del self.prices[item]

    def update_price(self, item, new_price):
        self.prices[item] = new_price

    def list_items(self):
        return self.items

    def find_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def __str__(self):
        menu_str = "Menu:\n"
        for category in self.categories:
            menu_str += f"{category}:\n"
            for item, price in self.prices.items():  
                if item.category == category:  
                    menu_str += f"{item} - ${price}\n"
        return menu_str


class Order:
    def __init__(self, table_number):
        self.items = []
        self.table_number = table_number
        self.status = "pending"
        self.total_price = 0

    def add_item(self, item):
        self.items.append(item)
        self.total_price += item.price

    def remove_item(self, item):
        self.items.remove(item)
        self.total_price -= item.price

    def calculate_total(self):
        return self.total_price

    def update_status(self, status):
        self.status = status

    def __str__(self):
        order_str = f"Order for Table {self.table_number}:\n"
        for item in self.items:
            order_str += f"{item.name} - ${item.price}\n"
        order_str += f"Total Price: ${self.total_price}\nStatus: {self.status}"
        return order_str

restaurant = Restaurant("Sultan Dain","Gulshan","10:00 AM")
menu = restaurant.Menu  # Accessing the Menu instance of the restaurant

menu.add_item(item="Rice", category="Dry", price=100)  # Removed 'subcategory' argument

order = Order(table_number=1)

print(restaurant)
print(menu)
print(order)
