# Ex 107:Avoiding Duplicates. solved 21 lines
# In this exercise, you will create a program that reads words from the user until the user enters a blank line.
# After the user enters a blank line your program should display each word entered by the user exactly once. The words
# should be displayed in the same order that they were entered. For example, if the user enters:
# >>> first / >>> second / >>> first / >>> third / >>> second ---> then your program should display:
# >>> first / >>> second / >>> third

user_list = []   # list user_list will contain all words added by user without duplicates
word = None

# loop will run and asks user to enter the word until user enters blank line
while word != '':
    word = input("Please, enter your word or blank line to exit: ")
    # if entered word by user not a blank line and not duplicate, the word is added to the user's list
    if word != '' and word not in user_list:
        user_list.append(word)

# display each of the entered by the user words without duplicates
print("\nYou have entered following words (without duplicates): ")
for word in user_list:
    print(word)
