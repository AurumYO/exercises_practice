# Ex 126: Generate All Sublists of a List. solved 40 lines
# Using the definition of a sublist from Exercise 125, write a function that returns a list containing every possible
# sublist of a list. For example, the sublists of [1, 2, 3], [], [1], [2], [3], [1, 2], [2, 3] and [1, 2, 3].
# Note that your function will always return a list containing at least the empty list because the empty list is a
# sublist of every list. Include a main program that demonstrate your function by displaying all of the sublists
# of several different lists.


# this function generates all sub-lists of a given list
def sublists_generator(input_list):
    # create copy of original list, new list list to store sub-lists, timer and loop counter to  loop through the list
    user_list, sublists = list(input_list), [],
    t, loop_counter = 0, len(user_list)
    # loop through the copy of original list for as many times as the length of the list passed to the the function
    while t < loop_counter:
        for num in range(len(user_list)+1):
            # add to the sub-lists part of the copy of original lists starting from the first position to the last
            sublists.append(user_list[:num])
        # increase the counter by 1 and delete first position from the copy of the original list
        t += 1
        user_list.pop(0)
    # clearing our sub-lists from duplicates and return the list of sub-lists
    result = []
    for item in sublists:
        if item not in result:
            result.append(item)
    return result


# this function demonstrates program performance
def main():
    input_list = [1, 2, 3]
    sublists = sublists_generator(input_list)
    print("The sublists for list {} are {} ".format(input_list, sublists))
    input_list = [7, 2, 3, 12]
    sublists = sublists_generator(input_list)
    print("The sublists for list {} are {} ".format(input_list, sublists))


if __name__ == '__main__':
    main()
