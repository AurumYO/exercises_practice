# Ex 76:Prime Factors
# Write a program that reads an integer from the user. If the value entered by the user is less than 2 then your program
# should display an appropriate error message. Otherwise your program should display the prime numbers that can be
# multiplied together to compute n, with one factor appearing on each line.

print("This program display the prime factors of a number.")

number = int(input("Please enter your number here: "))
factor = 2
print("The prime factors of {0} are: ".format(number))

while factor <= number:
    if number % factor == 0:
        print(factor)
        number = number / factor
    else:
        factor += 1

print("End!")
