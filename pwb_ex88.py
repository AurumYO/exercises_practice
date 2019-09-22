# Ex 88: Is it a Valid Triangle? solved 33 lines
# If you have 3 straws, possibly of differing lengths, it may or may not be possible to lay them down so that they form
# a triangle when their ends are touching. For example, if all of the straws have a length of 6 inches.
# then one can easily construct an equilateral triangle using them. However, if one straw is 6 inches. long, while the
# other two are each only 2 inches. long, then a triangle cannot be formed. In general, if any one length is greater
# than or equal to the sum of the other two then the lengths cannot be used to form a triangle. Otherwise they can form
# a triangle.
# Write a function that determines whether or not three lengths can form a triangle. The function will take 3 parameters
# and return a Boolean result. In addition, write a program that reads 3 lengths from the user and demonstrates the
# behaviour of this function.
print("This program will tell if it is a valid triangle.")


# this function takes 3 parameters with lengths of teh triangle and define if they can form triangle or not
def tirangle_validator(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        return 'is not a valid triangle'
    else:
        return 'is a valid triangle'


# this function asks for lengths of 3 sides from user and tels if they can form triangle or not
def main():
    a = int(input("Please length of the first straw: "))
    b = int(input("Please length of the second straw: "))
    c = int(input("Please length of the third straw: "))
    print("The straws with lengths {}, {}, {} when put together {}.".format(a, b, c, tirangle_validator(a, b, c)))


if __name__ =='__main__':
    main()
