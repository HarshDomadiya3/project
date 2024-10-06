def select_role():
    print("WELCOME TO FRUIT MARKET")
    print("1) Manager")
    print("2) Customer")
    
    role_choice = int(input("Select your Role (1 or 2): "))
    fruit_stock = {
        'Apple': {'qty': 50, 'price': 3.0},  
        'Banana': {'qty': 100, 'price': 1.0},
        'Orange': {'qty': 80, 'price': 2.0}
    }

    if role_choice == 1:
        def fruit_market_manager():
            while True:
                print("\nFruit Market Manager")
                print("1) Add Fruit Stock")
                print("2) View Fruit Stock")
                print("3) Update Fruit Stock")

                choice = int(input("Enter your choice: "))
                if choice == 1:
                    def add_fruit_stock():
                        fruit_name = input("Enter fruit Name: ")
                        qty = float(input("Enter qty (in kg): "))
                        price = float(input("Enter price (for kg): "))
                        if fruit_name in fruit_stock:
                            fruit_stock[fruit_name]['qty'] += qty
                            fruit_stock[fruit_name]['price'] = price
                        else:
                            fruit_stock[fruit_name] = {'qty': qty, 'price': price}
                        print(f"{fruit_name} added/updated in the stock.")
                    add_fruit_stock()
                elif choice == 2:
                    def view_fruit_stock():
                        print("\nCurrent Fruit Stock:")
                        for fruit, details in fruit_stock.items():
                            print(f"{fruit}: {details['qty']} kg available at {details['price']} per kg")
                        print()
                    view_fruit_stock()
                elif choice == 3:
                    def update_fruit_stock():
                        fruit_name = input("Enter the fruit name to update: ")
                        if fruit_name in fruit_stock:
                            qty = float(input(f"Enter the new qty (current: {fruit_stock[fruit_name]['qty']} kg): "))
                            price = float(input(f"Enter the new price (current: {fruit_stock[fruit_name]['price']} per kg): "))
                            fruit_stock[fruit_name]['qty'] = qty
                            fruit_stock[fruit_name]['price'] = price
                            print(f"{fruit_name} has been updated in the stock.")
                        else:
                            print(f"{fruit_name} does not exist in the stock.")
                    update_fruit_stock()
                else:
                    print("Invalid choice. Please try again.")
                more_operations = input("Do you want to more operations (press y for yes and n for no): ").lower()
                if more_operations != "y":
                    break
        fruit_market_manager()

    elif role_choice == 2:
        def fruit_market_customer():
            while True:
                print("\nFruit Market Customer")
                print("1) View Available Fruits")
                print("2) Purchase Fruit")

                choice = int(input("Enter your choice: "))
                if choice == 1:
                    def view_available_fruits():
                        print("\nAvailable Fruits:")
                        for fruit, details in fruit_stock.items():
                            print(f"{fruit}: {details['qty']} kg available at {details['price']} per kg")
                        print()
                    view_available_fruits()
                elif choice == 2:
                    def purchase_fruit():
                        fruit_name = input("Enter the fruit you want to purchase: ")
                        if fruit_name in fruit_stock:
                            qty_to_buy = float(input(f"How many kg of {fruit_name} would you like to buy? "))
                            if qty_to_buy <= fruit_stock[fruit_name]['qty']:
                                total_cost = qty_to_buy * fruit_stock[fruit_name]['price']
                                fruit_stock[fruit_name]['qty'] -= qty_to_buy
                                print(f"You purchased {qty_to_buy} kg of {fruit_name} for ${total_cost}.")
                            else:
                                print(f"Sorry, we only have {fruit_stock[fruit_name]['qty']} kg of {fruit_name}.")
                        else:
                            print(f"Sorry, {fruit_name} is not available.")
                    purchase_fruit()
                else:
                    print("Invalid choice. Please try again.")
                more_operations = input("Do you want to more operations (press y for yes and n for no): ").lower()
                if more_operations != "y":
                    break
        fruit_market_customer()

    else:
        print("Invalid choice. Please select either 1 (Manager) or 2 (Customer).")

select_role()

