import os

os.system('cls' if os.name == "nt" else 'clear')

# We will create a virtual store.

# We will create a list of products and another list containing their prices.
# The application will have a menu to allow user interaction.

"""
Menu
1. Add a product to the cart
2. View the shopping cart
3. Complete the order
4. Exit
"""

# When completing the order, the total amount to be paid will be displayed.
# If the cart is empty, the order cannot be completed.

# Available products in the store
products = ["Laptop", "Phone", "Headphones", "Mouse", "Keyboard"]
prices = [3500, 2000, 150, 100, 200]

shopping_cart = []


while True:  # Main loop that will run until the user chooses to exit
    print(f"\n\n{"*"*30}")
    print("Welcome to the store")
    print("Available products:")
    
    for i in range(len(products)):  # Iterate through each product in the product list: 0, 1, 2, 3, 4
        # Display product ID, name, and price
        print(f'{i + 1}. {products[i]} - {prices[i]} RON')  

    print()

    print("User Menu")
    print('1. Add a product to the cart')
    print('2. View the shopping cart')
    print('3. Complete the order')
    print('4. Exit')

    # Start of user input handling
    # Check if userInput is an integer between 1 and 4
    userInput = 0
    while True:
        try:
            userInput = int(input("Enter your choice: "))
        except ValueError:
            print("Not an integer!")
            continue
        else:
            if 1 <= userInput <= 4:
                print("A valid choice!")
                break
            else:
                print("An integer, but not a valid choice!")
                continue

    # Process user choice
    if userInput == 1:
        product = 0

        # Check if product ID is an integer between 1 and 5
        while True:
            try:
                product = int(input("Enter product ID: "))
            except ValueError:
                print("Not an integer!")
                continue
            else:
                if 1 <= product <= 5:
                    print("A valid choice!")
                    break
                else:
                    print("An integer, but not a valid choice!")
                    continue
        
        # Initialize the shopping cart if it's empty
        if not shopping_cart:
            for i in products:
                shopping_cart.append(0)

        shopping_cart[product - 1] += 1  # Add the selected product to the cart

    elif userInput == 2:
        print(f"Cart contents: {shopping_cart}")

    elif userInput == 3:
        total_price = 0         
        print("Your cart contains:\n")
        for i in range(len(shopping_cart)):
            if shopping_cart[i] != 0:
                total_price += shopping_cart[i] * prices[i]
                print(f"{shopping_cart[i]} {products[i]}  {shopping_cart[i]} * {prices[i]} = {shopping_cart[i] * prices[i]} RON")
        if not any(shopping_cart):
            print("The cart is empty.")
        print(f"Total amount to pay: {total_price} RON")
        
    else:
        if not any(shopping_cart):
            print("Your cart is empty, and your order cannot be completed.")
            continue
        else:
            print("Your cart contains:\n")
            for i in range(len(shopping_cart)):
                print(f"{shopping_cart[i]} {products[i]} {shopping_cart[i] * prices[i]} RON")
            print("Goodbye.")
        break

