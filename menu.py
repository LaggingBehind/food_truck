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