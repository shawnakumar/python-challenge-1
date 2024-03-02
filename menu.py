# Description: This program allows a customer to order from a food truck

# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
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
print ("-------------")
for k1,v1 in menu.items():
    print(k1)
    for k2,v2 in v1.items():
        print('\t',k2, end='')
        if isinstance(v2, dict):
            print()
            for k3,v3 in v2.items():
                print('\t\t', k3, v3)
        else:
             print(v2)

print("------xx------")
print ("-------------")
#print("From which menu would you like to order? ")
#for ix, k1 in enumerate(menu):
#    print(f'{ix+1}. {k1}')

#1 Setup the order list that will store a list of dictionaries for 
#menu items, prices, and quantities available for the customer to order
# Empty list to store the customer's order
order_list = []
print("order_list", order_list)
# Launch the store and present a welcome message for the customer
print("Welcome to the variety food truck!")
# Customers may want to order multiple items so create a continuous loop for taking orders
place_order = True
while place_order:
    # Get the menu category from the customer on what they would like to order
    print("From which menu would you like to order? ")
    #create a variable to store the menu category
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}
    # Print the options to choose from menu headings (all the first level dictionary items in menu)
    # Print menu categories
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key  
        # Store category for later retrieval
        #add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu item to view or q to quit: ")
#exit the loop if user typed 'q'
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
        print("Item # | Item name                | Price")
        print("-------|--------------------------|-------")
        for key, value in menu[menu_category_name].items():
            # Check if the menu item is a dictionary to handle differently
            if isinstance(value, dict):
                for key2, value2 in value.items():
                    num_item_spaces = 24 - len(key + key2) - 3
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                    menu_items[i] = {
                        "Item name": key + " - " + key2,
                        "Price": value2
                    }
                    i += 1
            else:
                num_item_spaces = 24 - len(key)
                item_spaces = " " * num_item_spaces
                print(f"{i}      | {key}{item_spaces} | ${value}")
                menu_items[i] = {
                    "Item name": key,
                    "Price": value
                }
                i += 1
            # 2. Ask customer to input menu item number
            menu_item = input("Type menu item number: ")

            # 3. Check if the customer typed a number
            if menu_item.isdigit():
                quantity = 1
                # Convert the menu selection to an integer
                menu_item = int(menu_item)
                # 4. Check if the menu selection is in the menu items
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
                        print("You didn't select a number.")

                    # Add the item name, price, and quantity to the order list
            else:
                quantity = 1
               
                # Convert the menu selection to an integer
                menu_item = int(menu_item)
                # 4. Check if the menu selection is in the menu items
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
                        print("You didn't select a number.")

                    # Add the item name, price, and quantity to the order list
                    order_list.append({
                        "Item name": item_name,
                        "Price": menu_items[menu_item]["Price"],
                        "Quantity": quantity
                    })
                    # Tell the customer that their input or quantity isn't valid
                    print("You didn't select a number.")

                # Tell the customer they didn't select a menu option

    else:
        # Tell the customer they didn't select a menu option
        print(f"{menu_category} was not a menu option.")

    while True:
        # Ask the customer if they would like to keep ordering
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
        #check if the customer intput is s Y or N
        # 5. Check the customer's input
        if keep_ordering.lower() == 'y':
            # Keep ordering
            break
        elif keep_ordering.lower() == 'n':
            # Complete the order
            print("Order completed.")
            # Since the customer decided to stop ordering, thank them for
            # their order
            print("Thank you for your order.")
            # Exit the keep ordering question loop
            place_order = False
            break
    else:
        # Tell the customer to try again
        print("Please try again.")

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
    print(order_list)

    # 8. Calculate the number of spaces for formatted printing'
    num_item_spaces = 24 - len(item_name)

    # 9. Create space strings
    item_spaces = " " * num_item_spaces

    # 10. Print the item name, price, and quantity
    print(f"{item_name}{item_spaces}| ${item['Price']} | {item['Quantity']}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
total = sum([item["Price"] * item["Quantity"] for item in order_list])
total_cost = sum(item['Price'] * item['Quantity'] for item in order_list)
print(f"Total Cost of the Order: ${total_cost:.2f}")
