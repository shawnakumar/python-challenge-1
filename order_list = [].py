order_list = []
print("order_list", order_list)
# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")
# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")
    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}
    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1
    # Get the customer's input
    menu_category = input("Type menu number to view or q to quit: ")
    #print(f"How many of the  {menu.menu_items} item would you like to order?")
    # Exit the loop if user typed 'q'
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
                if type(value) is dict:
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
            menu_selection = input("Please enter the number of the menu item you would like to select:")
            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)
                # 4. Check if the menu selection is in the menu items
                if menu_selection in menu_items.keys():
                    # Store the item name as a variable
                    item_name = menu_items[menu_selection]["Item name"]
                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"How many {item_name} would you like to order? (Default is 1): ")
                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():
                        quantity = int(quantity)
                    else:
                        quantity = 1
                        # Tell the customer that their input isn't valid
                        print("Invalid quantity input. Defaulting to 1.")
                    # Add the item name, price, and quantity to the order list
                    order_list.append({
                        "Item name": item_name,
                        "Price": menu_items[menu_selection]["Price"],
                        "Quantity": quantity})
                else:
                    # Tell the customer they didn't select a menu option
                    print("You didn't select a valid menu option.")
            else:
                    # Tell the customer they didn't select a menu option
                    print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")
    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
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
            print("Please enter a valid input (Y for Yes, N for No).")
# Print out the customer's order
print("This is what we are preparing for you.\n")
# Uncomment the following line to check the structure of the order
print(order_list)
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the order list to print them.
for item in order_list:
    # 7. Store the dictionary items as variables
    item_name = item['Item name']
    price = item['Price']
    quantity = item['Quantity']
    
    # 8. Print the item name, price, and quantity
    print(f"{item_name:25} | ${price:<8} | {quantity}")

# 9. Calculate the total cost of the order using list comprehension
total_cost = sum(item['Price'] * item['Quantity'] for item in order_list)

# 10. Print the total cost
print(f"\nTotal Cost: ${total_cost:.2f}")