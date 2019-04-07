# Exercise 74: Multiplication Table. soled 18 lines
# In this exercise you will create a program that displays a multiplication table that shows the products of all
# combinations of integers from 1 times 1 up to and including 10 times 10. Your multiplication table should include a
# row of labels across the top of it containing the numbers 1 through 10. It should also include labels down the left
# side consisting of the numbers 1 through 10. The expected output from the program is shown in exapml.
# When completing this exercise you will probably find it helpful to be able to print out a value without moving down to
# the next line. This can be accomplished by added end="" as the last parameter to your print statement. For example,
# print("A") will display the letter A and then move down to the next line. The statement print("A", end="") will
# display the letter A without moving down to the next line, causing the next print statement to display its result
# on the same line as the letter A.
print("This program shows the multiplication table for multiplications from 1 to 10.")
x, y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print first line with 4 spaces for
print('    ', end='')
for n in x:
    print('{:4d}'.format(n), end='')
# print out each next line 
for i in y:
    print()
    print('{:4d}'.format(i), end='')
    for j in x:
        print('{:4d}'.format(i * j), end="")
