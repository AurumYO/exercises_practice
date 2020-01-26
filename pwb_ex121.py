# Ex 121: Count the Elements (Solved—49 Lines)
# Python’s standard library includes a method named count that determines how many times specific value occurs in list.
# In this exercise, you will create a new function named countRange which determines and returns the number of elements
# within a list that are greater than or equal to some minimum value and less than some maximum value. Your function
# will take three parameters: the list, the minimum value and the maximum value. It will return an integer result
# greater than or equal to 0. Include a main program that demonstrates your function for several different lists,
# minimum and maximum values. Ensure that your program works correctly for both lists of integers and lists of floating
# point numbers.


# function takes list of integers, min and max value, and counts how many elements in the list are >= min and <= max
def count_range(user_list, min_value, max_value):
    # when function starts running counter is 0
    counter = 0
    # function runs through all list and compares each element to minimal and maximal value
    for n in user_list:
        # if element in the list is greater or equal to min value of smaller or equal to max value, counter increased
        if min_value <= n <= max_value:
            counter += 1
    # function returns number of elements which greater or equal to min value of smaller or equal to max value
    return counter


# the main function demonstrates counter_range function performance
def main():
    integers_list, min_value, max_value = [1, 2, 3, 4, 5], 2, 4
    print("Integers list {} contains {} elements which are greater/equal to {} and smaller/equal to {}.".
          format(integers_list, count_range(integers_list, min_value, max_value), min_value, max_value))
    floats_list, min_value, max_value = [9.0, 8, 7.0, 8, 4, 6, 3, 1, 1.2], 6, 8
    print("Integers list {} contains {} elements which are greater/equal to {} and smaller/equal to {}.".
          format(floats_list, count_range(floats_list, min_value, max_value), min_value, max_value))
    one_element_list,  min_value, max_value = [1], 6, 8
    print("Integers list {} contains {} elements which are greater/equal to {} and smaller/equal to {}.".
          format(one_element_list, count_range(one_element_list, min_value, max_value), min_value, max_value))
    zero_list,  min_value, max_value = [], 1, 5
    print("Integers list {} contains {} elements which are greater/equal to {} and smaller/equal to {}.".
          format(zero_list, count_range(zero_list, min_value, max_value), min_value, max_value))


if __name__ == '__main__':
    main()
