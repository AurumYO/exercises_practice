# Exercise 31: Sum of the Digits in an Integer. Develop a program that reads a four-digit integer from the user and
# displays the sum of the digits in the number. For example, if the user enters 3141 then your program
# should display 3 + 1 + 4 + 1 = 9.

print("This program reads the integers and display their sum")

# Ask for integers input from user
integers = str(input("Please enter as many integers as you like here: "))

integ = list(integers)

sum_integers = 0
for i in integ:
    sum_integers += int(i)
print(sum_integers)
