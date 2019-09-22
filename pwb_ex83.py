# Ex 83: Shipping Calculator. solved 23 lines
# An online retailer provides express shipping for many of its items at a rate of $10.95 for the first item, and
# $2.95 for each subsequent item. Write a function that takes the number of items in the order as its only parameter.
# Return the shipping charge for the order as the function’s result. Include a main program that reads the number of
# items purchased from the user and displays the shipping charge.
print("This program calculates the taxi fare.")
print()


# this functions takes numbers of items in parcel as parameters and computes the total shipping costs
def shipping_calculator(number_items):
    return number_items * 10.95 + number_items - 1 * 2.95 if number_items > 0 else 0


# this function demonstrates the function on shipping fee calculations
def main():
    number_items = int(input("Please enetr the number of items you want to ship: "))
    fee = shipping_calculator(number_items)
    print("The shipping fee for shipping {} item(s) is ${}.".format(number_items, fee))


if __name__ == '__main__':
    main()
