# Ex 106: Remove Outliers. Solved 43 lines.
# When analysing data collected as part of a science experiment it may be desirable to remove the most extreme values
# before performing other calculations. Write a function that takes a list of values and an non-negative integer, n,
# as its parameters. The function should create a new copy of the list with the n largest elements and the n smallest
# elements removed. Then it should return the new copy of the list as the function’s only result. The order of the
# elements in the returned list does not have to match the order of the elements in the original list.
# Write a main program that demonstrates your function. Your function should read a list of numbers from the user and
# remove the two largest and two smallest values from it. Display the list with the outliers removed, followed by the
# original list. Your program should generate an appropriate error message if the user enters less than 4 values.


# This function takes as argument list of integers and number of outliers,
# it removes defined quantity of outliers from largest and smallest values from the original list
# and returns new list without defined number of smallest and largest values from the original list
def outliers_remove(original_list, outliers_number):
    outliers_removed_list = sorted(original_list)      # original list sorted by ascending values
    # function loops n times, which is equal to number of outlines user wants to exclude
    for i in range(outliers_number):
        outliers_removed_list.pop()                    # remove last from behind value
        outliers_removed_list.pop(0)                   # remove first from the beginning value
    # function return new list without defined number of outliers of max and min values
    return outliers_removed_list


# Main function demonstrates performance of the function from outliers remove

def main():
    user_list = []
    # function reads values fro user until the Enter button pressed instead of input
    val = input("Please enter your value here, or 'Enter' to quit: ")
    while val != '':
        user_list.append(float(val))
        val = input("Please enter your value here, or 'Enter' to quit: ")
    # function asked to enter the user number of the outliers to remove
    outliers_number = int(input("Please, enter number of outliers to remove: "))
    # report that the entered number of values to small to process data
    if len(user_list) < 4:
        print("You have entered less than 4 values. Too little data to process!")
    # display of the outcome of the function from outliers remove and original list
    else:
        print("\nYour list with removed outliers is following: {}".format(outliers_remove(user_list, outliers_number)))
        print("And your original list looked like this: {}".format(user_list))


if __name__ == '__main__':
    main()
