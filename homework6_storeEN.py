'''
- We will create a virtual store -

- We will create a list of products and another list containing their prices.
- The application will have a menu to allow user interaction.

"
Menu
1. Add a product to the cart
2. View the shopping cart
3. Complete the order
4. Exit
"

- When completing the order, the total amount to be paid will be displayed.
- If the cart is empty, the order cannot be completed.
'''

# Available products in the store
products = ["Laptop", "Telephone", "Headphone", "Mouse", "Keyboard"]
prices = [3500, 2000, 150, 100, 200]

shopping_cart = []

while True:  # Main loop that will run until the user chooses to exit
    print("Welcome to the store")
    print("Available products:")
    
    for i in range(len(products)):  # Iterate through each product in the product list: 0, 1, 2, 3, 4
        # Display product ID, name, and price
        print(f'{i + 1}. {products[i]} - {prices[i]} RON')

    print("User Menu")
    print('1. Add a product to the cart')
    print('2. View the shopping cart')
    print('3. Complete the order')
    print('4. Exit')

    # Ask the user to choose an option from the menu
    option = input("Choose an option: ")
    
    if option == "1":
        # Subtract 1 from input because, in our list, the first product is at index 0.
        # If we don't subtract 1, the user selecting "1" would pick "Telephone" instead of "Laptop."
        product_index = int(input("Choose the desired product: ")) - 1
        if 0 <= product_index < len(products):
            shopping_cart.append((products[product_index], prices[product_index]))
            print(f'The product added to the cart: {products[product_index]}.')
        else:
            print("The selected product is not available.")
    
    # The user chooses to view the shopping cart
    # Check if there are any products in the cart
    # Display the products in the cart
    # Iterate through each product in the cart
    # Display each product and its price
    # Display the total cart value
    elif option == "2":
        if len(shopping_cart) > 0:
            print('*' * 30)
            print("\nProducts in your cart:")
            print('*' * 30)
            total = 0  # Initialize total amount
            for product, price in shopping_cart:
                print('-' * 30)
                print(f'The product is {product} and its price is {price} RON')
                print('-' * 30)
                total += price
            print(f'The total value of the shopping cart is {total} RON')
        else:
            print("There are no products in the cart.")
            
    # The user wants to complete the order
    # Check if there are products in the cart
    # Display products
    # Calculate the total cart value
    # Show a confirmation message for the placed order
    # Exit the program
    # If there are no products, display a message that the order cannot be completed
    elif option == "3":
        if len(shopping_cart) > 0:
            print("\nCompleting the order ...")
            total = 0
            for product, price in shopping_cart:
                total += price
            print(f'Your order has been placed! Total payment: {total} RON.')
            break
        else:
            print("Your cart is empty, and the order cannot be completed.")
            
    # The user chooses to exit the application
    # Display a "Goodbye!" message
    # Stop the application
    elif option == "4":
        print("Goodbye!")
        break
    
    # Otherwise, display that the entered option is invalid
    else:
        print('!' * 30)
        print("The option does not exist in the menu.")
        print('!' * 30)

