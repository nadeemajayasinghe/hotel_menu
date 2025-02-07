# Define the menu of the restaurant
menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80,
    'Tea': 20,
    'Water': 10,
    'Ice Cream': 30,
    'Coke': 20,
}


# Welcome message and menu display
print("Welcome to our Restaurant!\n")
print("Here is the menu")
for item, price in menu.items():
    print(f"{item} : Rs.{price}")

# Initialize order total
order_total = 0


# Function to take order
def take_order():
    global order_total
    while True:
        # Ask the user for the item name
        item = input("\nEnter the name of the item you want to order: ").strip()
        if item in menu:
            order_total += menu[item]
            print(f"Your item '{item}' has been added to your order.")
        else:
            print(f"Sorry, '{item}' is not available in the menu.")

        # Ask if they want to order more
        another_order = input("Do you want to order another item? (Yes/No): ").strip().lower()
        if another_order != 'yes':
            break

# Call the function to start ordering
take_order()


# Print the total amount to pay
print(f"\nThe total amount to pay is: Rs.{order_total}")
print("Thank you for ordering with us!")
