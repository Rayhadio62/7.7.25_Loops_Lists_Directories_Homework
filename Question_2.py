# Menu items and prices
menu = {
    1: ("Pizza", 15.99),
    2: ("Burger", 12.50),
    3: ("Salad", 9.99),
    4: ("Pasta", 13.75)
}
drink_price = 2.50
tax_rate = 0.08

# Display the menu
print("=== RESTAURANT MENU ===")
for number, (item, price) in menu.items():
    # {:.2f} means "format as a floating-point number with 2 decimal places.
    print(f"{number}. {item} - ${price:.2f}")
# Get user's food choice
choice = int(input("\nEnter your choice (1-4): "))
# Check if choice is valid
if choice not in menu:
    print("Invalid choice. Please restart the program.")
else:
    food_name, food_price = menu[choice]

    # Ask about drink
    drink_input = input("Would you like a drink? (+$2.50) (yes/no): ").strip().lower()
    has_drink = drink_input == "yes"
    drink_cost = drink_price if has_drink else 0.00

    # Calculate costs
    subtotal = food_price + drink_cost
    tax = subtotal * tax_rate
    total = subtotal + tax

    # Display itemized bill
    print("\n=== YOUR ORDER ===")
    print(f"Food: {food_name} - ${food_price}")
    print(f"Drink: {'Yes' if has_drink else 'No'} - ${drink_cost}")
    print(f"Subtotal: ${subtotal}")
    print(f"Tax (8%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")