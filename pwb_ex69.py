# Ex 69: Approximate π. The value of π can be approximated by the following infinite series:
# ....
# Write a program that displays 15 approximations of π . The first approximation should make use of only the first term
# from the infinite series. Each additional approximation displayed by your program should include one more term in the
# series, making it a better approximation of π than any of the approximations displayed previously
print("This program makes Pi aproximation.")
x, y, z = 2, 3, 4
# prompt user to enter the number of decimal points after approximation
approximation = int(input("Please enter number of decimal points after approximation: "))
pi = 3
counter = 1

while counter < approximation:
    if counter % 2 != 0:
        pi += 4 / (x * y * z)
        x += 2
        y += 2
        z += 2
        counter += 1
    if counter % 2 == 0:
        pi -= 4/(x * y * z)
        x += 2
        y += 2
        z += 2
        counter += 1
# display the approximation  result of Pi (with max 15 decimal points)
print("The approximation of Pi of {0} times is equal to {1:.15f}".format(approximation, pi))
