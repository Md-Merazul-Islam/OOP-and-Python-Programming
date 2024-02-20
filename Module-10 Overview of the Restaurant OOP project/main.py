from Menu import *
from restaurant_ import *
from user import *
from order import *


def main():
    menu = Menu()
    # for pizzaas
    Pizza_1 = Pizza("Shutki pizza", 500, "Large", ["Shutki", 'Oil', "ata"])
    Pizza_2 = Pizza("Meat pizza", 600, "Large", ["Meat", 'Oil', "ata"])
    Pizza_3 = Pizza("Milk pizza", 400, "Small", ["Milk", 'Oil', "ata"])
    menu.add_menu_item('pizza', Pizza_1)
    menu.add_menu_item('pizza', Pizza_2)
    menu.add_menu_item('pizza', Pizza_3)

    # for burgers
    Burger_1 = Burger("Chicken Burger", 300, "Chiken",
                      ["chicken", 'oil', 'Moyda'])
    Burger_2 = Burger("Cow Burger", 600, "Cow", ["Cow", 'oil', 'Moyda'])
    Burger_3 = Burger("Fish Burger", 200, "Fish", ["Fish", 'oil', 'Moyda'])
    menu.add_menu_item('burger', Burger_1)
    menu.add_menu_item('burger', Burger_2)
    menu.add_menu_item('burger', Burger_3)

    # for Drink
    Drink_1 = Drink("Lemon", 200, True)
    Drink_2 = Drink("Orange", 300, False)
    Drink_3 = Drink("Tea", 50, False)
    menu.add_menu_item('drink', Drink_1)
    menu.add_menu_item('drink', Drink_2)
    menu.add_menu_item('drink', Drink_3)

    # show  menu
    menu.show_menu()

    restaurant = Restaurant("Sultan dine", 2000, menu)

    # add employees
    manager = Manager("Rohim", 35408, "rohim@gmail.com",
                      "dhaka", 2000, "2 jan 2023", "managment")
    restaurant.add_employee('manager', manager)

    chef = Chef("Rakib", 8778, "rakib@gmail.com", "gazipur",
                2003, "2 sep 2022", 'Chef', 'cooking')
    restaurant.add_employee('chef', chef)

    server = Server("Ratif", 3434, "asdhlk@gmail.com",
                    "koriya", 220, '2 march 2022', 'server')
    restaurant.add_employee('server', server)

    # show customer
    restaurant.show_employees()

    # customer 1 placing an order
    Customer_1 = Customer("Meraz", 987, "akdshf@gamil.com", "asdhkf", 12000)
    order_1 = Order(Customer_1, [Pizza_1, Drink_1, Drink_2, Pizza_2, Burger_1])
    Customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)
    restaurant.receiver_payment(order_1, 20000, Customer_1)
    print(f'revenue : {restaurant.revenue} , Balance : { restaurant.balance}')

    # customer 2 placing an order
    Customer_2 = Customer("hisam", 463006, "asdf@gamil.com", "afg", 34)
    order_2 = Order(Customer_2, [Pizza_2, Drink_3, Drink_1, Pizza_1, Burger_3])
    Customer_2.pay_for_order(order_2)
    restaurant.add_order(order_2)
    restaurant.receiver_payment(order_2, 100000, Customer_2)
    print(f'revenue : {restaurant.revenue} , Balance : { restaurant.balance}')

    restaurant.pay_expense(restaurant.rent,'rent')
    print(f'after rent : ')
    print(f'revenue : {restaurant.revenue} , Balance : { restaurant.balance} Expense : {restaurant.expense}')

    restaurant.pay_salary(chef)
    print(f'after salary pay  : ')
    print(f'revenue : {restaurant.revenue} , Balance : { restaurant.balance} Expense : {restaurant.expense}')
    

if __name__ == "__main__":

    main()
