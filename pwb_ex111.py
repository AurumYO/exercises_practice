# Exercise 111: Only the Words. solved 38 lines.
# In this exercise you will create a program that identifies all of the words in a string entered by the user. Begin by
# writing a function that takes a string of text as its only parameter. Your function should return a list of the words
# in the string with the punctuation marks at the edges of the words removed. The punctuation marks that you must remove
# include commas, periods, question marks, hyphens, apostrophes, exclamation points, colons, and semicolons. Do not
# remove punctuation marks that appear in the middle of a words, such as the apostrophes used to form a contraction.
# For example, if your function is provided with the string "Examples of contractions include: don’t, isn’t,
# and wouldn’t." then your function should return the list ["Examples", "of", "contractions", "include", "don’t",
# "isn’t", "and", "wouldn’t"].
# Write a main program that demonstrates your function. It should read a string from the user and display all of the
# words in the string with the punctuation marks removed. You will need to import your solution to this exercise when
# completing Exercise 158. As a result, you should ensure that your main program only runs when your file has not been
# imported into another program.


# This functions converts any string to list with words
def only_words(string):
    new_string = ''
    punctuations = '""\':;,.!?-'                        # store all punctuation marks we need to exclude
    # loop through each letter in string and if not punctuation sign for exclusion add letter to new list
    for char in string:
        if char not in punctuations and char != ' ':   # exclude also spaces to handle them differently
            new_string += char
        if char == ' ' and new_string[-1] != ' ':  # check that previous character not space to exclude excess spaces
            new_string += char
    new_string = new_string.strip(' ')             # remove spaces in beginning and at the end of the line if any
    word_list = new_string.split(' ')              # split cleaned from punctuation signs string to separate words
    return word_list                               # function returns list of words


# main function prompts user to enter the string of words and display the words from string cleaned from punctuation
def main():
    user_string = str(input("Please enter your string: "))
    result = only_words(user_string)
    print("The entered string contains following words:")
    print(only_words(user_string))
    # testing of the function performance
    assert only_words("Examples of contractions include: don’t, isn’t, and wouldn’t.") == \
           ['Examples', 'of', 'contractions', 'include', 'don’t', 'isn’t', 'and', 'wouldn’t']
    assert only_words('In addition?, "the" word "and"  - is normally included! .') \
           == ['In', 'addition', 'the', 'word', 'and', 'is', 'normally', 'included']
    assert only_words('?what??.;') == ['what']

main()
