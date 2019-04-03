# Exercise 33: Day Old Bread. A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
# percent. Write a program that begins by reading the number of loaves of day old bread being purchased from the user.
# Then your program should display the regular price for the bread, the discount because it is a day old,
# and the total price. All of the values should be displayed using two decimal places, and the decimal points in all
# of the numbers should be aligned when reasonable values are entered by the user.

print("This program shows price of the day ld bread of the bakery.")
print()
# Asking for the user input
quantity_dayoldbread = int(input("Please, enter the quantity of day old bread you would like to byu: "))
# Define the price for fresh bread
price_freshbread = float(3.49)

# Calculate check prices
total_price = quantity_dayoldbread * price_freshbread
# calculate amount of discount
discount = round(float(total_price * 0.4), 2)
# Calculated amount tdue to payments including 60% discount
due_payment = round(float(total_price - discount), 2)
# Display the output of the program
print('''Yor due to payment amount is:
    the total price for {:d} loafs is {:0.2f}$,
    discount for the day old bread of 60% amounts -{:0.2f}$
    the total amount is {:0.2f}$.'''.format(quantity_dayoldbread, total_price, discount, due_payment))
