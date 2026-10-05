"""
Week 2 Assignment: Simple Bill Calculator

Asks the user for the price of one item and the quantity they want,
calculates the total, and prints a friendly summary.
"""

price = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity: "))

total = price * quantity

print(f"{quantity} items at {price:.2f} each = {total:.2f}")
