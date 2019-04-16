# Ex 78: Decimal to Binary. Write a program that converts a decimal (base 10) number to binary (base 2). Read the
# decimal number from the user as an integer and then use the division algorithm shown below to perform the conversion.
# When the algorithm completes, result contains the binary representation of the number. Display the result, along with
# an appropriate message.

print("This program converts decimal number to binary.")
decimal_num = int(input("Please enter your decimal number here: "))

res = ''
r = decimal_num % 2
res = str(r) + res
q = decimal_num // 2

while q > 0:
    r = q % 2
    res = str(r) + res
    q = q // 2

print("The decimal number {0} in binary system is equal to {1}.".format(decimal_num, res))
