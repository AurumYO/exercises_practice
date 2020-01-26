# Ex 129: Exercise 128: Reverse Lookup (Solved—40 Lines)


# This function finds all of the keys in a dictionary that map to a specific value.
# Function takes the dictionary and the value to search for as its only parameters, returning (possibly
# empty) list of keys from the dictionary that map to the provided value.
def reverse_lookup(input_dict, value):
    keys = []                       # variable keys will store names of the keys where stored searched value
    # loop through the dictionary and if searched value found append to the keys list name of the key signed to variable
    for k, v in input_dict.items():
        if value == v:
            keys.append(k)
    return keys


# Main program that demonstrates the reverse_lookup function as part of solution to this exercise
# program should create a dictionary and then show that the reverse_lookup function works correctly when it returns
# multiple keys, a single key, and no keys.
def main():
    # generate dictionary of fruits with
    fruits = ['oranges', 'apples', 'grapes', 'lemons', 'lime', 'oranges', 'apples', 'grapes']
    test_dictionary = {}
    for i in range(8):
        k = 'fruit#' + str(i)
        test_dictionary.update({k: fruits[i]})
    # demonstration of the function performance
    print("In given dictionary: ", test_dictionary)
    print("We search for value {} in our dictionary.".format(fruits[0]))
    res = reverse_lookup(test_dictionary, 'oranges')
    print("Searched value {} found in keys: {}".format(fruits[0], res))
    res2 = reverse_lookup(test_dictionary, 'lime')
    print("Searched value {} found in keys: {}".format(fruits[4], res2))
    res3 = reverse_lookup(test_dictionary, 'banana')
    print("Searched value {} found in keys: {}".format('banana', res3))


if __name__ == '__main__':
    main()
