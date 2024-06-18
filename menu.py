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