""" John has 5 apples, and he buys 7 more from the market. If he gives 3
apples to his friend, how many apples does he have left? Write a Python
program to solve this."""
john_apples = 5
new_apples = john_apples + 7
remaining_apples = new_apples - 3
print(remaining_apples)
print("**************************************************")
print()

"""A store gives a 10% discount if a customer spends $100 or more. 
Write a Python program that asks for the total amount spent and prints
the final amount to be paid after applying the discount (if applicable).
"""
def store_discount(spending):
    total_amount = 0
    discount = 10/100
    if spending >= 100:
        total_amount = spending - (spending * discount)
    else:
        total_amount = spending
    return total_amount

customer = store_discount(150)
print(customer)
