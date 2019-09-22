# Ex 109: List of Proper Divisors. Solved 36 lines.
# A proper divisor of a positive integer, n, is a positive integer less than n which divides evenly into n.
# Write a function that computes all of the proper divisors of a positive integer. The integer will be passed to the
# function as its only parameter. The function will return a list containing all of the proper divisors as its only
# result. Complete this exercise by writing a main program that demonstrates the function by reading a value from the
# user and displaying the list of its proper divisors. Ensure that your main program only runs when your solution has
# not been imported into another file.


# this function finds all proper divisors for positive integer
# function takes any positive integer as its argument
def proper_divisors(n):
    proper_divisors_list = []                   # empty list which will contain all proper divisors for given number
    # function loops any positive integer greater than 0 and smaller than given number n
    for number in range(1, n):
        # when given number is divided evenly by any number > 0 and < given number n
        if n % number == 0:
            proper_divisors_list.append(number)  # such even divisor added to the list of proper divisors
    # function returns list of all proper divisors of given number n
    return proper_divisors_list


# Main function calls for input of the positive integer from user
# calls for proper_divisor function to get list of proper divisors for user's number and
# displays all proper divisors for user's number
def main():
    n = int(input("Please, enter the number greater than 0 here: "))
    proper_divisors_list = proper_divisors(n)
    print("Proper divisors for number {:d} are {}".format(n, proper_divisors_list))


if __name__ == '__main__':
    main()