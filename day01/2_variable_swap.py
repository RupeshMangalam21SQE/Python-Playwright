# Swaps two numbers entered by the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Before swap: a = {a}, b = {b}")
a, b = b, a
print(f"After swap: a = {a}, b = {b}")