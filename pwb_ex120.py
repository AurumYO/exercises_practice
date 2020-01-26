# Ex 120:Is a List already in Sorted Order? (41 Lines)
# Write a function that determines whether or not a list of values is in sorted order (either ascending or descending).
# The function should return True if the list is already sorted. Otherwise it should return False. Write a main program
# that reads a list of numbers from the user and then uses your function to report whether or not the list is sorted.
# Make sure you consider these questions when completing this exercise: Is a list that is empty in sorted order?
# What about a list containing one element?


# this function takes list and defines if the list is sorted (returning True) or not (returns False) in descending or
# ascending order. If list has 1 element - than list is sorted. If no elements in list it returns False
def is_list_sorted(user_list):
    if len(user_list) == 1:     # if list has only 1 element function returns True
        return True
    # variables to count how many elements in list are greater or less than following element
    ascending_counter, descending_counter = 0, 0
    # loop through list and compare each element with following element. since list starts with 0 index
    # make sure function not overlaps the length of teh list
    for x in range(len(user_list)-1):
        a, b = user_list[x], user_list[x + 1]    # to compare element with following element's value
        if a < b:  # if first element smaller than following element
            ascending_counter += 1     # increase counter of ascending elements
        elif a > b:  # if first element bigger than following element
            descending_counter += 1    # increase counter of descending elements
    # If counter of ascending/descending elements smaller by 1 than length of list, than all compared elements
    # are smaller or greater than next standing element and list is sorted
    if ascending_counter == len(user_list) - 1 or descending_counter == len(user_list) - 1:
        return True
    else:              # else list is not sorted
        return False


# main function prompts user to input integers for their list and defines if entered numbers to list are in sorted order
def main():
    user_list = []
    element = input("Please enter number to your string of numbers here or blank line to stop: ")
    # loop runs and asks user for input of integer until blank line entered
    while element != '':
        user_list.append(int(element))
        element = input("Please enter number to your string of numbers here or blank line to stop: ")
    # main program calls function 'is_list_sorted' to define if entered list of integers are in sorted order
    result = is_list_sorted(user_list)
    # function displays appropriate message with definition if list is sorted or not
    if result:
        print("The list {} is in sorted order.".format(user_list))
    else:
        print("The list {} is not in sorted order.".format(user_list))


if __name__ == '__main__':
    main()
