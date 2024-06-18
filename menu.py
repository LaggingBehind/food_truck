# Starter code with menu items
menu_items = {
    1: ("Hamburger", 3.99),
    2: ("Fries", 1.99),
    3: ("Soft Drink", .99),
    4: ("Coffee",.50)
}


# Function to print menu
def print_menu():
    print("Menu:")
    for key, value in menu_items.items():
        print(f"{key}. {value[0]} - ${value[1]:.2f}")

# Order list to stores customer
order_list = []

# Funtion to add items to order
def add_to_order(item_name, price, quantity):
    order_list.append({
        "Item name": item_name,
        "price": price,
        "Quantity": quantity
    })
    
# Main program to take orders and print receipt
def take_order():
    while True:
        print_menu()
        menu_selection = input("Please enter the menu item number you would like: ")
        
        # Validate menu_selection
        if not menu_selection.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        
        menu_selection = int(menu_selection)
        
        if menu_selection not in menu_items:
            print("Invalid selsction. Please choose valid item number.")
            continue
        
        # Get item details from menu
        item_name, price = menu_items[menu_selection]
        
        # Get quantity
        quantity_input = input(f"How many of {item_name} would you like to order?")
        
        if not quantity_input.isdigit():
            print(f"Inavlid input for quantity. defaulting quantity to 1.")
            quantity = 1
        else:
            quantity = int(quantity_input)
            
        # Add item to order list
        add_to_order(item_name, price, quantity)
        
        # Ask if the customer wants to continue ordering
        while True:
            continue_ordering = input("Would you like to order another item? (y/n): ")
            if continue_ordering == "y":
                place_order = True
                break
            elif continue_ordering == "n":
                place_order = False
                print("Thank you for your order.")
                break
            else:
                print("Invalid intput. Please enter y or n.")
                
        if not place_order:
            break
        
# Print receipt
    print("\nReceipt")
    print("Item name            | Price | Quantitiy")
    print("---------------------|-------|----------")
    total_price = 0
    for order in order_list:
        item_name = order["Item name"]
        price = order["Price"]
        quantity = order["Quantity"]
        total_price += price * quantity
        
        # Calculate spaces for formatting
        spaces_item = " " * (26 - lan(item_name))
        spaces_price = " " * (7 - len(f"${price:.2f}"))
        spaces_quantity = " " * (9 - len(str(quantity)))
        
        # Print the order line
        print(f"{item_name}{spaces_item}| ${price:.2f}{spaces_price}| {quantity}{spaces_quantity}")
        
    # Print total price