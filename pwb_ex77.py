# Ex: 77. Binary to Decimal. Write a program that converts a binary (base 2) number to decimal (base 10). Your
# program should begin by reading the binary number from the user as a string. Then
# it should compute the equivalent decimal number by processing each digit in the
# binary number. Finally, your program should display the equivalent decimal number
# with an appropriate message.

print("This program converts binary number to decimal.")

binary_num = int(input("Please enter your binary number here: "))
binary = binary_num
decimal, i = 0, 0

while binary != 0:
    dec = binary % 10
    decimal = decimal + dec * pow(2, i)
    binary = binary // 10
    i += 1

print("The binary number {} in decimal system is equal to {}.".format(binary_num, decimal))
