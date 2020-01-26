# Exercise 125: Does a List contain a Sublist? (44 Lines)
# A sublist is a list that makes up part of a larger list. Create a function, isSublist, that determines whether or not
# one list is a sublist of another. Your function should take two lists, larger and smaller, as its only parameters.
# It should return True if and only if smaller is a sublist of larger. Write a main program that demonstrates function.


# Function defines if smaller list is sublist of the larger list. Function takes two lists - smaller and larger
def is_sublist(smallest, largest):
    # Define an temporary lists to compare sublist
    sublist, comparable_sublist = [], []
    # Define two constants to iterate in the while loop
    i = 0
    k = 0
    # Loop  through thr length of the largest list
    while i < len(largest):
        # If the element is in the smallest list program append element to temporary list
        if k < len(smallest) and largest[i] == smallest[k]:
            sublist.append(largest[i])
            # set a comparable lists to the value of temporary list
            comparable_sublist = sublist
            k += 1
            # If the comparable list is the same as the smallest list  - break
            if len(comparable_sublist) == len(smallest):
                break
        # If the element is not in the smallest list reset temporary list
        else:
            sublist = []
        i += 1
    # Function returns as result comparison between temporary comparable lists with smallest list from input
    return comparable_sublist == smallest


# Main function demonstrates performance of the function is_sublist()
def main():
    assert is_sublist([1], [1, 2, 3, 4]) == True, "[1] is sublist of [1, 2, 3, 4]"
    assert is_sublist([2], [1, 2, 3, 4]) == True, "[2] is sublist of [1, 2, 3, 4]"
    assert is_sublist([3], [1, 2, 3, 4]) == True, "[3] is sublist of [1, 2, 3, 4]"
    assert is_sublist([4], [1, 2, 3, 4]) == True, "[4] is sublist of [1, 2, 3, 4]"
    assert is_sublist([2, 3], [1, 2, 3, 4]) == True, "[2, 3] is sublist of [1, 2, 3, 4]"
    assert is_sublist([2, 4], [1, 2, 3, 4]) == False, "[2, 4] is not sublist of [1, 2, 3, 4]"
    assert is_sublist([], [1, 2, 3, 4]) == True, "[] is sublist of [1, 2, 3, 4]"
    assert is_sublist([1, 2, 3, 4], [1, 2, 3, 4]) == True, "[1, 2, 3, 4] is sublist of [1, 2, 3, 4]"

    smalest, largest = [1, 6], [1, 2, 3, 4]
    result = is_sublist(smalest, largest)
    if result:
        print("The {} is a sublist of {}".format(smalest, largest))
    else:
        print("The {} is not a sublist of {}".format(smalest, largest))


if __name__ == '__main__':
    main()
