# Ex. 113: Formatting a List. Solved 43 lines
# When writing out a list of items in English, one normally separates the items with commas. In addition, the word “and”
# is normally included before the last item, unless the list only contains one item. Consider the following four lists:
#   apples
#   apples and oranges
#   apples, oranges and bananas
#   apples, oranges, bananas and lemons
# Write a function that takes a list of strings as its only parameter. Your function should return a string that
# contains all of the items in the list formatted in the manner described previously as its only result. While the
# examples shown previously only include lists containing four elements or less, your function should behave correctly
# for lists of any length. Include a main program that reads several items from the user, formats them by calling your
# function, and then displays the result returned by the function.


# This function takes list of string as its arguments and makes formatting inserting  comma after each string, unless
# the string item is second from behind - than function places and after such item and places no character after
# the last string. Function returns the formatted string of values from list with strings.
def list_formater(list):
    if len(list) == 1:
        return list[0]
    elif len(list) == 2:
        return list[0] + ' and ' + list[1]
    else:
        formatted_list = ''
        for item in list[:-2]:
            formatted_list = formatted_list + item + ', '

        return formatted_list + list[-2] + ' and ' + list[-1]


# Main function prompts user to enter the the words as strings or plank line to stop making inputs
# calls function for formatting list and displays the formatted list of strings entered by user
def main():
    strings_list = []
    user_string = str(input("Please enter your string or blank line to stop enter: "))
    while user_string != '':
        strings_list.append(user_string)
        user_string = str(input("Please enter your string or blank line to stop enter: "))

    formatted_list = list_formater(strings_list)
    print(formatted_list)


if __name__ == '__main__':
    main()
