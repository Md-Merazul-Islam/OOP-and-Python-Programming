from shopping import*
from user import*
from product import*

def main():
    shopping = Shopping("Jamuan")
    meraz = shopping.add_user("meraz@gmail.com", "1111", "buyer")
    rakin = shopping.add_user("rakin@gmail.com", "2222", "buyer")
    admin1 = shopping.add_user("admin1@gmail.com", "3333", "seller")
    admin2 = shopping.add_user("admin2@gmail.com", "2222", "seller")
    shopping.add_product(1, "shosha", 20, 0)
    shopping.add_product(2, "moric", 24, 2)
    shopping.add_product(3, "lebui", 40, 2)
    shopping.add_product(4, "am", 50, 2)
    shopping.add_product(5, "jam", 60, 2)
    current_user = None

    while True:
        if current_user is None:
            print("Please sign up or login")
            option = input("Login or Register (L/R): ")
            
            #loging--->
            if option == 'L':
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                match = False
                for user in shopping.users:
                    if user['email'] == email and user['password'] == password:
                        current_user = user
                        match = True
                        break
                if not match:
                    print("No user found!")
                else:
                    print(f"_____________Welcome back______ {current_user['email']}!_________")
                    if current_user['type'] == 'seller':
                        print("\nOptions:")
                        print("1: Add Products")
                        print("2: Show all available products")
                        print("3: Logout")
                        option = input("Enter your option: ")
                        if option == '1':
                            id = input("Enter product id: ")
                            name = input("Enter product name: ")
                            price = input("Enter product price: ")
                            quantity = input("Enter product quantity: ")
                            shopping.add_product(id, name, price, quantity)
                            print(f'Products added successfully.')
                        elif option == '2':
                            shopping.show_products_list()
                        elif option == '3':
                            current_user = None

                    elif current_user['type'] == 'buyer':
                        print("\nOptions:")
                        print("1: Show product list")
                        print("2: Buy item")
                        print("3: Logout")
                        option = input("Enter your option: ")
                        if option == '1':
                            shopping.show_products_list()
                        elif option == '2':
                            product_id = input("Enter product id: ")
                            buyer_balance = float(input("Enter your balance: "))
                            Product.buy_product(shopping, product_id, buyer_balance)
                        elif option == '3':
                            current_user = None
                    
                    
                    
            #Register--->
            elif option == 'R':
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                user_type = input("Are you a buyer or a seller? : ")
                if user_type not in ["buyer", "seller"]:
                    print("Invalid user type.")
                    continue
                user = shopping.add_user(email, password, user_type)
                current_user = user
                print("Your account register successfully.Thankyou.")
                # print(f"_____________Welcome______, {current_user['email']}!_________")
                if current_user['type'] == 'seller':
                    print("\nOptions:")
                    print("1: Add Products")
                    print("2: Show all available products")
                    print("3: Logout")
                    option = input("Enter your option: ")
                    if option == '1':
                        id = input("Enter product id: ")
                        name = input("Enter product name: ")
                        price = input("Enter product price: ")
                        quantity = input("Enter product quantity: ")
                        shopping.add_product(id, name, price, quantity)
                    elif option == '2':
                        shopping.show_products_list()
                    elif option == '3':
                        current_user = None

                elif current_user['type'] == 'buyer':
                    print("\nOptions:")
                    print("1: Show product list")
                    print("2: Buy item")
                    print("3: Logout")
                    option = input("Enter your option: ")
                    if option == '1':
                        shopping.show_products_list()
                    elif option == '2':
                        product_id = input("Enter product id: ")
                        buyer_balance = float(input("Enter your balance: "))
                        Product.buy_product(shopping, product_id, buyer_balance)
                    elif option == '3':
                        current_user = None
        else:
            # print(
            #     f"_____________Welcome______, {current_user['email']}!_________")
            if current_user['type'] == 'seller':
                print("\nOptions:")
                print("1: Add Products")
                print("2: Show all available products")
                print("3: Logout")
                option = input("Enter your option: ")
                if option == '1':
                    id = input("Enter product id: ")
                    name = input("Enter product name: ")
                    price = input("Enter product price: ")
                    quantity = input("Enter product quantity: ")
                    shopping.add_product(id, name, price, quantity)
                elif option == '2':
                    shopping.show_products_list()
                elif option == '3':
                    current_user = None

            elif current_user['type'] == 'buyer':
                print("\nOptions:")
                print("1: Show product list")
                print("2: Buy item")
                print("3: Logout")
                option = input("Enter your option: ")
                if option == '1':
                    shopping.show_products_list()
                elif option == '2':
                    product_id = input("Enter product id: ")
                    buyer_balance = float(input("Enter your balance: "))
                    Product.buy_product(shopping, product_id, buyer_balance)
                elif option == '3':
                    current_user = None


if __name__ == '__main__':
    main()
