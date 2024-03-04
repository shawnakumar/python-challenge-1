# Description: This program allows a customer to order from a food truck
# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": 0.99,
        "Banana": 0.69,
        "Apple": 0.49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}
# Print the menu
print("-------------")
for k1, v1 in menu.items():
    print(k1)
    for k2, v2 in v1.items():
        print('\t', k2, end='')
        if isinstance(v2, dict):
            print()
            for k3, v3 in v2.items():
                print('\t\t', k3, v3)
        else:
            print(v2)
print("------xx------")
print("-------------")
# Setup the order list that will store a list of dictionaries for 
# menu items, prices, and quantities available for the customer to order
# Empty list to store the customer's order
order_list = []
print("order_list", order_list)
# Launch the store and present a welcome message for the customer
print("Welcome to the variety food truck!")
# Customers may want to order multiple items, so create a continuous loop for taking orders
place_order = True
while place_order:
    # Get the menu category from the customer on what they would like to order
    print("From which menu would you like to order? ")
    # create a variable to store the menu category
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}
    # Print the options to choose from menu headings (all the first level dictionary items in menu)
    # Print menu categories
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key  
        # Store category for later retrieval
        # add 1 to the menu item number
        i += 1
    # Get the customer's input
    menu_category = input("Type menu item to view or q to quit: ")
    # exit the loop if the user typed 'q'
    # Check if the customer's input is a number
    if menu_category == 'q':
        break
    # Check if the customer's input is a number 
    if menu_category.isdigit(): 
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():           
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")
            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            # After selecting a category and printing "What [Category] item would you like to order?"
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            i = 1
            menu_items = {}
            for key, value in menu[menu_category_name].items():
                if isinstance(value, dict):
                    for key2, value2 in value.items():
                        print(f"{i}      | {key} - {key2}{' ' * (24 - len(key + key2) - 3)} | ${value2}")
                        menu_items[i] = {"Item name": f"{key} - {key2}", "Price": value2}
                        i += 1
                else:
                    print(f"{i}      | {key}{' ' * (24 - len(key))} | ${value}")
                    menu_items[i] = {"Item name": key, "Price": value}
                    i += 1
            # 2 Now, outside the loop, prompt for the user's selection
            # Inside the while place_order loop, after printing the menu items for the selected category
            # Prompt for the user's selection
            menu_item = input("Type the number of the menu item you would like to select: ")
            # Check if the user input is a string before using isdigit()
            if isinstance(menu_item, str) and menu_item.isdigit():
                # Convert the menu selection to an integer
                menu_item = int(menu_item)
                
            if menu_item in menu_items:
                # Correctly retrieve the selected item details
                selected_item = menu_items[menu_item]
                item_name = selected_item["Item name"]
                item_price = selected_item["Price"]
                # Ask for the quantity of the selected item
                quantity_input = input(f"How many of {item_name} would you like to order? ")
                if quantity_input.isdigit():
                    quantity = int(quantity_input)
                else:
                    print("Invalid input. Defaulting to 1.")
                    quantity = 1
                # Add the selected item and quantity to the order list
                order_list.append({
                    "Item name": item_name,
                    "Price": item_price,
                    "Quantity": quantity
                })
                print(f"Added {quantity} of {item_name} to your order.")
            else:
                print("You didn't select a valid menu option.")
    # 3 Check if the customer typed a number
    elif menu_category.isdigit():
        QUANTITY = 1
        # Convert the menu selection to an integer
        menu_item = int(menu_category)
        # Check if the menu selection is in the menu items
        if menu_item in menu_items:
            # Store the item name as a variable
            item_name = menu_items[menu_item]["Item name"]
            # Ask the customer for the quantity of the menu item
            quantity = input(f"How many {item_name} would you like to order? ")
            # Check if the quantity is a number, default to 1 if not
            if quantity.isdigit():
                # Add the item name, price, and quantity to the order list
                order_list.append({
                    "Item name": item_name,
                    "Price": menu_items[menu_item]["Price"],
                    "Quantity": int(quantity)
                })
            else:
                print("You didn't select a menu option.")
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    while True:
        # Ask the customer if they would like to keep ordering
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
        # Check if the customer input is s Y or N
        # 5. Check the customer's input
        match keep_ordering.lower():
            case "y":
                place_order = True
                # Continue ordering
                break
            case "n":
                place_order = False
                # Stop ordering and complete the order
                print("Thank you for your order.")
                break
            case _:
                print("You didn't enter a Y or N. Please try again.")
            # Complete the order
# Print out the customer's order
print("This is what we are preparing for you.\n")
# Uncomment the following line to check the structure of the order
# print(order)
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")
# 6. Loop through the items in the customer's order
for item in order_list:
    # 7. Store the dictionary items as variables
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]
   # print(order_list)
    # 8. Calculate the number of spaces for formatted printing
    num_item_spaces = 26 - len(item_name)
    num_price_spaces = 5 - len(str(price))
    # 9. Create space strings
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces
    # 10. Print the item name, price, and quantity
    print(f"\n{item_name}{item_spaces}| ${item['Price']}{price_spaces} | {item['Quantity']}")
# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
print("\n--------------------------|--------|----------")
total_cost = sum(item['Price'] * item['Quantity'] for item in order_list)
print(f"Total Cost of the Order: ${total_cost:.2f}")
