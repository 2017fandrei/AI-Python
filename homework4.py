'''
# Extra exercise
# 1. Read two variables, number1 and number2, of type float, from the user.
# 2. Read a variable operation that can be "+", "-", "*", or "/". If "stop" is entered, the program stops.
# 3. Using if, elif, and else, perform the requested operation between number1 and number2 and display the result.
# 4. If the operation is invalid, stop the program.
# 5. Use a while loop to repeat the steps above until the user enters "stop".


# 1. Numbers from 1 to 10
# Write a program that displays all the numbers from 1 to 10 using a for loop.


# 2. Even numbers between 1 and 20
# Write a program that displays all the even numbers between 1 and 20 using a while loop.


# 3. Sum of the first 10 integers
# Write a program that calculates and displays the sum of the first 10 integers (from 1 to 10 inclusive) using a for loop.


# 4. Countdown
# Write a program that displays a countdown from 10 to 1 using a while loop.


# 5. Odd numbers between 1 and 15
# Write a program that displays all the odd numbers between 1 and 15. Use a for loop and an if condition.


# 6. Check if a number is positive
# Write a program that reads an integer from the user and checks if it is positive, negative, or zero.
# Display an appropriate message.


# 7. Digits of a number
# Write a program that reads an integer from the user and displays each digit of the number on a new line.
# Use a while loop to extract the digits.


# 8. Numbers divisible by 3 between 1 and 30
# Write a program that displays all numbers between 1 and 30 that are divisible by 3. Use a for loop and the modulo operator (%).


# 9. Display the squares of numbers from 1 to 10
# Write a program that displays the square of each number from 1 to 10 using a for loop.
# Display the results in the format "Number: Square".


# 10. Average of entered numbers
# Write a program that reads 5 integers from the user and calculates their average.
# Use a for loop to read and add the numbers, then divide the sum by 5 to get the average.
'''

ex1='''
1. Numbers from 1 to 10
Write a program that displays all the numbers from 1 to 10 using a for loop.
'''
print(ex1)
for i in range(1,11):
    print(i, end=" ")
print()  # Adds a final newline
"""
The extra % sign you see in your zsh shell output after using print(i, end=" ") occurs because Python does not automatically print a newline when using end=" ", and the % symbol is part of the zsh shell prompt indicating that the cursor is still on the same line.
"""

ex2='''
2. Even numbers between 1 and 20
Write a program that displays all the even numbers between 1 and 20 using a while loop.
'''
print(ex2)
i = 1
while i <= 20:
    if i%2 == 0:
        print(i, end=" ")
    i += 1
print()

# Here's another approach.
print("Here's another approach.")
i=1
if i%2 == 1:
    i += 1
while i <= 20:
    print(i, end=" ")
    i += 2
print()

ex3='''
3. Sum of the first 10 integers
Write a program that calculates and displays the sum of the first 10 integers (from 1 to 10 inclusive) using a for loop.
'''
print(ex3)
sum = 0
for i in range(1,10):
    sum += i
sum += i + 1
print(sum)

# Here's another approach.
print("Here's another approach.")
sum = 0
for i in range(1,11):
    sum += i
print(sum)

# Here's the last approach.
print("Here's the last approach.")
sum=(1+10)*10/2
print(sum)

ex4='''
4. Countdown
Write a program that displays a countdown from 10 to 1 using a while loop.
'''
print(ex4)
i=10
while i >= 1:
    print(i, end=" ")
    i -= 1
print()

ex5='''
5. Odd numbers between 1 and 15
Write a program that displays all the odd numbers between 1 and 15. Use a for loop and an if condition.
'''
print(ex5)
for i in range(1,15+1):
    if i%2 == 1:
        print(i, end=" ")
print()

ex6='''
6. Check if a number is positive
Write a program that reads an integer from the user and checks if it is positive, negative, or zero.
Display an appropriate message.

'''
print(ex6)
# check first if user input is an integer
userInput = 0
while True:
  try:
     userInput = int(input("Enter an integer: "))
  except ValueError:
     print("Not an integer!")
     continue
  else:
     print("Yes an integer!")
     break

if userInput > 0:
    print(f"{userInput} is a positive integer.")
elif userInput < 0:
    print(f"{userInput} is a negative integer.")
else:
    print(f"{userInput} is zero.")

ex7='''
7. Digits of a number
Write a program that reads an integer from the user and displays each digit of the number on a new line.
Use a while loop to extract the digits.

'''
print(ex7)
nr = int(input("Enter an integer: "))

if nr == 0:
    print(nr)
elif nr < 0:
    nr *= -1

while nr:
    dig = nr%10
    print(dig)
    nr = nr // 10
