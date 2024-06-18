menu_items = {
    1: ("Hamburger", 3.99),
    2: ("Fries", 2.99),
    3: ("Coffee", 1.99),
    4: ("Coke", 1.99),
    5: ("Water", 1.00)
}

# Function to print the menu
def print_menu():
    print("Menu:")
    for key, value in menu_items.items():
        print(f"{key}. {value[0]} - ${value[1]:.2f}")

# Order list to store customer's order
order_list = []

# Function to add items to order
def add_to_order(item_name, price, quantity):
    order_list.append({
        "Item name": item_name,
        "Price": price,
        "Quantity": quantity
    })

# Main program to take orders and print receipt
def take_order():
    while True:
        print_menu()
        menu_selection = input("Please enter the menu item number you'd like to order: ")

        # Validate menu_selection
        if not menu_selection.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        menu_selection = int(menu_selection)
        
        if menu_selection not in menu_items:
            print("Invalid selection. Please choose a valid menu item number.")
            continue

        # Get item details from menu
        item_name, price = menu_items[menu_selection]

        # Get quantity
        quantity_input = input(f"How many of {item_name} would you like to order? ")
        
        if not quantity_input.isdigit():
            print(f"Invalid input for quantity. Defaulting quantity to 1.")
            quantity = 1
        else:
            quantity = int(quantity_input)
        
        # Add item to order list
        add_to_order(item_name, price, quantity)

        # Ask if the customer wants to continue ordering
        while True:
            continue_ordering = input("Would you like to order another item? (y/n): ").lower()
            if continue_ordering == 'y':
                break
            elif continue_ordering == 'n':
                print("Thank you for your order.")
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        if continue_ordering == 'n':
            break

    # Print receipt
    print("\nReceipt")
    print("Item name                 | Price  | Quantity")
    print("--------------------------|--------|----------")
    total_price = 0
    for order in order_list:
        item_name = order["Item name"]
        price = order["Price"]
        quantity = order["Quantity"]
        total_price += price * quantity

        # Calculate spaces for formatting
        spaces_item = " " * (26 - len(item_name))
        spaces_price = " " * (7 - len(f"${price:.2f}"))
        spaces_quantity = " " * (9 - len(str(quantity)))

        # Print the order line
        print(f"{item_name}{spaces_item}| ${price:.2f}{spaces_price}| {quantity}{spaces_quantity}")

    # Print total price
    print(f"\nTotal price: ${total_price:.2f}")

# Run the order system
take_order()