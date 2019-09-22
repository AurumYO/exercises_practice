# Exercise 85: Convert an Integer to its Ordinal Number. Solved 47 lines.
# Words like first, second and third are referred to as ordinal numbers. In this exercise, you will write a function
# that takes an integer as its only parameter and returns a string containing the appropriate English ordinal number as
# its only result. Your function must handle the integers between 1 and 12 (inclusive). It should return an empty
# string if a value outside of this range is provided as a parameter. Include a main program that demonstrates your
# function by displaying each integer from 1 to 12 and its ordinal number. Your main program should only run when your
# file has not been imported into another program.
print("This program coverts an integer to its ordinal number.")


# this function takes integer as argument and returns the ordinal number of the integers from 1 to 12
def integers_converter(n):
    # function contains dictionary from numbers and ordinal numbers pairs
    integers_orders = {1: 'first', 2: 'second', 3: 'third', 4: 'forth', 5: 'fifth', 6: 'sixth', 7: 'seventh',
                       8: 'eighth', 9: 'ninth', 10: 'tenth', 11: 'eleventh', 12: 'twelve'}
    # if integer is in range of dictionary keys, the function returns its ordinal number else returns empty string
    if n in integers_orders.keys():
        return ''.join(integers_orders[v] for v in integers_orders.keys() if v == n)
    else:
        return ''


# main funtion which prompts user to input the integer and displays the ordinal number for given integer from 1 to 12
def main():
    user_integer = int(input("Please enter your integer from 1 to 12: "))
    print("The ordinal number of {} is {}.".format(user_integer, integers_converter(user_integer)))


main()
