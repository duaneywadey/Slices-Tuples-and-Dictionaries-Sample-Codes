# Function to calculate the total price of an order
def process_order(order_list, order_name, quantity):
    price_per_order = order_list[order_name] 
    total_price = price_per_order * quantity 
    return total_price

# Dictionary of order names and their corresponding prices
order_list_prices = {
    "Burgers": 45,
    "Cheese sticks": 20,
    "Kwek-kwek": 20
}

# Display the menu to the user
print("Welcome to all! Here's the menu:")
for item, price in order_list_prices.items():
    print(f"{item}: {price} PHP")


# Prompt the user for order choice and quantity
print('''
    \nType 1 for Burgers 
    \nType 2 for Cheese sticks
    \nType 3 for Kwek-kwek''')

# Ask user for his order choice
order_name_choice = int(input("\nEnter your order choice: "))
how_many_orders = int(input("How many orders do you want?: "))

# Calculate and print the total price
print("\nTotal Price:")
if order_name_choice == 1:
    order_name = "Burgers"
elif order_name_choice == 2:
    order_name = "Cheese sticks"
elif order_name_choice == 3:
    order_name = "Kwek-kwek"
else:
    print("Invalid order choice!")
    exit()

# Invoke the process_order function
total_price = process_order(order_list_prices, order_name, how_many_orders)
print(total_price)
print("\nThank you for your order!")
