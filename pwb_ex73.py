# Ex.73: Multiple Word Palindromes. There are numerous phrases that are palindromes when spacing is ignored. Examples
# include “go dog”, “flee to me remote elf” and “some men interpret nine memos”, among many others. Extend your solution
# to Exercise 72 so that it ignores spacing while determining whether or not a string is a palindrome. For an additional
# challenge, extend your solution so that is also ignores punctuation marks and treats uppercase and lowercase letters
# as equivalent.
print("This program will tell if phrase is palindrome or not...")
# prompt user for input
string = str(input("Please enter your phrase here: "))

print("Method #1 - mine:")
string = string.lower()
new_string = ''
for l in string: # create new string where only letters go, dropping spaces, and other punctuations
    if l.isalpha():
        new_string += l

list_string = list(new_string)  # convert new string with letters to list
reversed_string = list_string.copy()  # create new list and apply list.reverse() method
reversed_string.reverse()

if list_string == reversed_string:  # comparing if original list equal to reversed list and print our conclusion
    print('The entered string "{0}" is palindrome.'.format(string))
else:
    print('The entered string "{0}" is not a palindrome.'.format(string))

print("Method #2 - solution from book:")
string = string.lower()
n_string = ''
for l in string: # create new string where only letters go, dropping spaces, and other punctuations
    if l.isalpha():
        n_string += l

is_palindrome = True
for i in range(0, len(n_string) //2 ):
    if n_string[i] != n_string[len(n_string) - i - 1]:
        is_palindrome = False

if is_palindrome:
    print('The entered string "{0}" is palindrome.'.format(string))
else:
    print('The entered string "{0}" is not a palindrome.'.format(string))