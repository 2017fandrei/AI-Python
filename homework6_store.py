# We will create a virtual store

# We will create a list of products and another list with the prices of the products.
# The application will have a menu so that the user can interact with it.

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
    print("Welcome to the store")
    print("Available products:")
    
    for i in range(len(products)):  # Iterate through each product in the product list: 0, 1, 2, 3, 4
        # 1. Product ID. Product - Price
        print(f'{i + 1}. {products[i]} - {prices[i]} RON')  # Display the product and its price

    print("User Menu")
    print('1. Add a product to the cart')
    print('2. View the shopping cart')
    print('3. Complete the order')
    print('4. Exit')
