message="""
Extra exercise
1. Read two variables, number1 and number2, of type float, from the user.
2. Read a variable operation that can be "+", "-", "*", or "/". If "stop" is entered, the program stops.
3. Using if, elif, and else, perform the requested operation between number1 and number2 and display the result.
4. If the operation is invalid, stop the program.
5. Use a while loop to repeat the steps above until the user enters "stop".
"""
print(message)

while True:

    print()
# 1. Read two variables, number1 and number2, of type float, from the user.
# is string input a float?
# check for two inputs
    while True:
      try:
         userInput = float(input("Enter first float: "))
      except ValueError:
         print("Not a float!")
         continue
      else:
         print("Yes a float!")
         break
    
    number1 = userInput
    
    while True:
      try:
         userInput = float(input("Enter second float: "))
      except ValueError:
         print("Not a float!")
         continue
      else:
         print("Yes a float!")
         break
    
    number2 = userInput

# 2. Read a variable operation that can be "+", "-", "*", or "/". If "stop" is entered, the program stops.
# 3. Using if, elif, and else, perform the requested operation between number1 and number2 and display the result.
# 4. If the operation is invalid, stop the program.
    
    operation = input("What operation would you like to perform with the two numbers? ")
    while operation not in ["+", "-", "*", "/", "stop"]:
        print("Invalid operation! Please try again.")
        operation = input("What operation would you like to perform with the two numbers? ")

    if operation == "stop":
        exit()
    elif operation == "+":
        print(f"{number1} + {number2} = {number1 + number2}")
        continue
    elif operation == "-":
        print(f"{number1} - {number2} = {number1 - number2}")
        continue
    elif operation == "*":
        print(f"{number1} * {number2} = {number1 * number2}")
        continue
    else:
        if number2 == 0:
            print("Division by zero is impossible! Please try again. ")
            continue
        else:
            print(f"{number1} / {number2} = {number1 / number2}")
            continue
    
