class Food:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        self.cooking_time = 15


class Burger(Food):
    def __init__(self, name, price, meat, ingredients) -> None:
        super().__init__(name, price)
        self.meat = meat
        self.ingredinets = ingredients


class Pizza (Food):
    def __init__(self, name, price, size, toppings) -> None:
        super().__init__(name, price)
        self.size = size
        self.toppings = toppings


class Drink(Food):
    def __init__(self, name, price, isClod=True) -> None:
        super().__init__(name, price)
        self.isClod = isClod


class Menu:
    def __init__(self) -> None:
        self.pizzas = []
        self.burgers = []
        self.drinks = []

    def add_menu_item(self, item_type, item):
        if item_type == 'pizza':
            self.pizzas.append(item)
        elif item_type == 'burger':
            self.burgers.append(item)
        elif item_type == 'drink':
            self.drinks.append(item)
        else:
            print('Invalid item!')

    def remove_pizza(self, pizza):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)

    def show_menu(self):
        print('Pizzas -----------> ')
        for pizza in self.pizzas:
            print(f'Name : {pizza.name} Price : {pizza.price}')
        print('Burgers -----------> ')
        for burger in self.burgers:
            print(f'Name : {burger.name} Price : {burger.price}')
        print('Drinks -----------> ')
        for drink in self.drinks:
            print(f'Name : { drink.name} Price : { drink.price}')
