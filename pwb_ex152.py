# Exercise 152: What’s that Element Again? (59 Lines)

# program that reads a file containing information about chemical elements and stores it in dictionary, where
# protons numbers are keys and in values are lists with symbol and name as elements of the list
elements_file = open('chemelements.txt', 'r')
elements_dict = {}
lines = elements_file.readlines()
elements_file.close()

# loop through each line, striping end of lines and obtaining list of elements with number of protons in first position,
# symbol in second element of the list and name of the element in third element in the list
for line in lines:
    details = line.strip().split(' ')
    # add to dictionary of elements number of protons as kes and list with symbol and name as value
    elements_dict[int(details[0])] = [details[1], details[2]]

# Then program should read and process input from the user
user_input = input("Please enter chemical element's name, symbol or number of protons; enter blank line to exit: ")
# Continue to read input from the user until a blank line is entered
while user_input != '':
    # If the user enters an integer then program displays the symbol and name of the element with the number of protons
    # entered.
    if user_input.isdigit() and int(user_input) in elements_dict.keys():
        print("{} protons has element with symbol '{}' which named {}.\n".
              format(user_input, elements_dict[int(user_input)][0], elements_dict[int(user_input)][1]))
    # If the user enters a string then program displays the number of protons for the element with that name or symbol
    elif user_input.isalpha():
        for k, v in elements_dict.items():
            if user_input == v[0] or user_input == v[1]:
                print("{} protons has element with symbol '{}' and with name {}.\n".format(k, v[0], v[1]))
    # appropriate error message if no element exists for the name, symbol or number of protons entered
    else:
        print("Wrong input. No elements with such name, symbol or number of protons!!!\n")

    user_input = input("Please enter chemical element's name, symbol or number of protons; enter blank line to exit: ")
