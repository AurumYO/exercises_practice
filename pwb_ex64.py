# Ex 64: No More Pennies. solved in 38 lines.
# Write a program that reads prices from the user until a blank line is entered. Display the total cost of all the
# entered items on one line, followed by the amount due if the customer pays with cash on a second line. The amount due
# for a cash payment should be rounded to the nearest nickel. One way to compute the cash payment amount is to begin by
# determining how many pennies would be needed to pay the total. Then compute the remainder when this number of pennies
# is divided by 5. Finally, adjust the total down if the remainder is less than 2.5. Otherwise adjust the total up.
print("This program computes the price due to payment rounded to nickels.")
print("Please enter the prices of goods you choose below.")
# prompt user to input all prices of the goods
prices = [float(x) for x in input("use ',' between prices and space to finish input: ").split(',')]
total_price = 0
# compute total gross amount of the purchase
for price in prices:
    total_price += price
print("The total price is ${}".format(total_price))
# compute approximation of the gross amount
if (total_price*100) % 5 == 0:
    total_price = total_price
elif (total_price*100) % 5 < 2.5:
    total_price = (((total_price*100) // 5)*5)/100
elif (total_price*100) % 5 >= 2.5:
    total_price = ((((total_price*100) // 5) + 1)*5)/100
# display the output of the program
print("The total price due to payment is ${0:.2f}".format(total_price))