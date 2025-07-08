# Get user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
quantity = int(input("How many tickets do you want? "))

# Determine ticket price based on age
if age < 13:
    ticket_type = "Child"
    ticket_price = 8.00
elif age <= 64:
    ticket_type = "Adult"
    ticket_price = 12.00
else:
    ticket_type = "Senior"
    ticket_price = 9.00

# Calculate total cost
total_cost = ticket_price * quantity
# Print receipt
print("\n=== MOVIE TICKET RECEIPT ===")
print(f"Customer: {name}")
print(f"Ticket Type: {ticket_type} (${ticket_price:.2f} each)")
print(f"Quantity: {quantity}")
print(f"Total Cost: ${total_cost:.2f}")
print("Thank you for your purchase!")