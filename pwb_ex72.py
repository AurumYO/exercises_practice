# Exercise 72: Is a String a Palindrome? (Solved—23 Lines)
# A string is a palindrome if it is identical forward and backward. For example “anna”, “civic”, “level” and “hannah”
# are all examples of palindromic words. Write a program that reads a string from the user and uses a loop to
# determines whether or not it is a palindrome. Display the result, including a meaningful output message.

print("This program will tell if string is palindrome or not...")
string = str(input("Please enter your string here: "))

print("Method #1 - mine:")
list_string = list(string)  # convert string to list
reversed_string = list_string.copy()  # create new list and apply list.reverse() method
reversed_string.reverse()

if list_string == reversed_string:  # comparing if original list equal to reversed list and print our conclusion
    print('The entered string "{0}" is palindrome.'.format(string))
else:
    print('The entered string "{0}" is not a palindrome.'.format(string))

print("Method #2 - solution from book:")
is_palindrome = True

for i in range(0, len(string) //2 ):
    if string[i] != string[len(string) - i - 1]:
        is_palindrome = False

if is_palindrome:
    print('The entered string "{0}" is palindrome.'.format(string))
else:
    print('The entered string "{0}" is not a palindrome.'.format(string))
