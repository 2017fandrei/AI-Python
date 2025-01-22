#!/usr/bin/env python3
"""
Define a list of 10 items.

1. Search for an item in a list using a for loop.
2. Calculate and display the sum of the elements in a list using a for loop.
3. Display the first 3 items in a list using slicing.
4. Display items in a list from middle to end using slicing.
5. Display items in a list at intervals of 2 using slicing.
6. Display inverted list using slicing.
7. Display items in a list from index 1 to 4 using slicing.
8. Display the last 3 items in a list using slicing.
9. Display the items in a list from the beginning to the penultimate item using slicing.
10. Display only items greater than 3 in a list using a for loop.
"""

# Define a list of 10 items.
ml = ["ab", 3.4, 5, [3, 4, 5], True, "random", "apple", "chatGPT", 9, 10]

############################################################################################
ex1 = """
1. Search for an item in the list using a for loop.
"""
############################################################################################
print(ex1, end="")
print(f"ml = {ml}\n")

# Check if the string "ab" exists in the list
for i in range(len(ml)):
    if ml[i] == "ab":
        print(f"The string 'ab' exists in ml.")

# Check if the float 3.4 exists in the list
for i in range(len(ml)):
    if ml[i] == 3.4:
        print(f"The float 3.4 exists in ml.")

# Check if the boolean True exists in the list
for i in range(len(ml)):
    if ml[i] == True:
        print(f"The boolean value True exists in ml.")

# Check if the list [3, 4, 5] exists in the list
for i in range(len(ml)):
    if ml[i] == [3, 4, 5]:
        print(f"The list [3, 4, 5] exists in ml.")

# Check if the integer 100 exists in the list
found = False
for i in range(len(ml)):
    if ml[i] == 100:
        found = True
        break

if found:
    print(f"The integer 100 exists in ml.")
else:
    print(f"The integer 100 does not exist in ml.")

############################################################################################
ex2 = """
2. Calculate and display the sum of the elements in a list using a for loop.
"""
############################################################################################
print(ex2)

mathL = [1, 3.4, 5, 7.00, 5.77, 4, 567, 44, 45, 10]
total_sum = 0  # Avoid using `sum` as it is a built-in function in Python
for el in mathL:
    total_sum += el  # Simplified addition with `+=`
print(f"The sum of the elements in {mathL} is {total_sum}.")


############################################################################################
ex3 = """
3. Display the first 3 items in a list using slicing.
"""
############################################################################################
print(ex3, end="")
print(f"ml = {ml}\n")
print(ml[:3])

############################################################################################
ex4 = """
4. Display items in a list from middle to end using slicing.
"""
############################################################################################
import math

print(ex4, end="")
print(f"ml = {ml}\n")
print(ml[math.floor(len(ml)/2):])

############################################################################################
ex5 = """
5. Display items in a list at intervals of 2 using slicing.
"""
############################################################################################
print(ex5, end="")
print(f"ml = {ml}\n")
print(ml[::2])


############################################################################################
ex6 = """
6. Display inverted list using slicing.
"""
############################################################################################
print(ex6, end="")
print(f"ml = {ml}\n")
print(ml[::-1])

############################################################################################
ex7 = """
7. Display items in a list from index 1 to 4 using slicing.
"""
############################################################################################
print(ex7, end="")
print(f"ml = {ml}\n")
print(ml[1:5])

############################################################################################
ex8 = """
8. Display the last 3 items in a list using slicing.
"""
############################################################################################
print(ex8, end="")
print(f"ml = {ml}\n")
print(ml[-3:])

############################################################################################
ex9 = """
9. Display the items in a list from the beginning to the penultimate item using slicing.
"""
############################################################################################
print(ex9, end="")
print(f"ml = {ml}\n")
print(ml[:-1])

############################################################################################
ex9 = """
10. Display only items greater than 3 in a list using a for loop.
"""
############################################################################################
print(ex9, end="")
ml = [-0, +0, -100, 300, 100, 44, -2345, 99, 101]
print(len(ml))
print(f"ml = {ml}\n")
for i in ml:
    if i > 3:
        print(i)
