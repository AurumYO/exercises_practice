# Exercise 102: Reduce Measures. Solved 83 lines.
# Many recipe books still use cups, tablespoons and teaspoons to describe the volumes of ingredients used when cooking
# or baking. While such recipes are easy enough to follow if you have the appropriate measuring cups and spoons,
# they can be difficult to double, triple or quadruple when cooking Christmas dinner for the entire extended family.
# For example, a recipe that calls for 4 tablespoons of an ingredient requires 16 tablespoons when quadrupled.
# However, 16 tablespoons would be better expressed (and easier to measure) as 1 cup.
# Write a function that expresses an imperial volume using the largest units possible. The function will take the number
# of units as its first parameter, and the unit of measure (cup, tablespoon or teaspoon) as its second parameter.
# Return a string representing the measure using the largest possible units as the function’s only result. For example,
# if the function is provided with parameters representing 59 teaspoons then it should return the string “1 cup,
# 3 tablespoons, 2 teaspoons”.


# This function converts inputted number of units teaspoons into cups, tablespoons and teaspoons
def teaspoon2cup_tablespoon(number_units):
    cup = number_units // 48               # 1 cup contains 48 teaspoons, finding number of full cups
    remaining = number_units % 48          # finding remainder of teaspoons after we calculated amount of full cups
    tablespoon = remaining // 3            # 1 tablespoon contains 3 teaspoons, finding number of full tablespoons
    teaspoon = remaining % 3               # finding remainder of teaspoons after we calculated amount of tablespoons
    return cup, tablespoon, teaspoon       # function returns tuple containing number of cups, tablespoons and teaspoons


# This function converts inputted number of tablespoons to cups, tablespoons and teaspoons
def tablespoon2cup_teaspoon(number_units):
    cup = number_units // 16               # 1 cup contains 16 tablespoons, finding number of full cups
    remaining = number_units % 16          # finding remainder of tablespoons after we calculated amount of full cups
    tablespoon = remaining                 # number of tablespoons will be equal of our remainder
    teaspoon = 0                           # since user inputted amount of tablespoons, we have zero teaspoons
    return cup, tablespoon, teaspoon       # function returns tuple containing number of cups, tablespoons and teaspoons


# This function performs conversion depending on the input from user
def make_conversion(number_units, type_units):
    if type_units == 1:                       # if user made input in cups which is our largest inputted unit
        # in result only number of cups remains, and no further calculation
        result = number_units, 0, 0           # number of tablespoons and teaspoons equal to zero
        return result                         # function return in result only number of cups
    if type_units == 2:                       # if user entered input in tablespoons
        result = tablespoon2cup_teaspoon(number_units)  # conversion to number of cups, tablespoons and teaspoons done
    if type_units == 3:                       # if user entered input in tablespoons
        result = teaspoon2cup_tablespoon(number_units)  # conversion number of to cups, tablespoons and teaspoons done
    return result                          # function returns user's input to number of cups, tablespoons and teaspoons


# This function displays the output of the program depending on the user's input
def display_output(number_units, type_units):
    result = make_conversion(number_units, type_units)        # called function to make conversion of inputted values
    if type_units == 1:                                # if user choose input in cups
        units_type = 'cups'                            # output message will contain cups as base input
    elif type_units == 2:                              # if user choose input in tablespoons
        units_type = 'tablespoons'                     # output message will contain tablespoons as base input
    elif type_units == 3:                              # if user choose input in teaspoons
        units_type = 'teaspoons'                       # output message will contain teaspoons as base input
    output = '{} {} will be'.format(number_units, units_type)  # output will contain user's units quantity and name
    # depending if result of conversion has in output cups, tablespoons and teaspoons,
    # the appropriate units quantity and name added to the final function output
    if result[0]:
        cup_output = ' {} cups'.format(result[0])
        output += cup_output
    if result[1]:
        tablespoon_output = ' and {} tablespoons'.format(result[1])
        output += tablespoon_output
    if result[2]:
        teaspoon_output = ' and {} teaspoons'.format(result[2])
        output += teaspoon_output
    output += "."
    # function returns output message
    return print(output)


# main  functions calls user to make input and displays the result of conversion to larger measurement units
def main():
    number_units = int(input("Please enter number of units here: "))
    type_units = int(input("Choose unit of measure by pressing - 1 for cup, 2 for tablespoon and 3 for teaspoon: "))
    display_output(number_units, type_units)


if __name__ == '__main__':
    main()

