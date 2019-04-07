# Ex 75: Exercise 75: Greatest Common Divisor. solved 17 lines.
# The greatest common divisor of two positive integers, n and m, is the largest number, d, which divides evenly into
# both n and m. There are several algorithms that can be used to solve this problem, including:
#  Initialize d to the smaller of m and n.
#  While d does not evenly divide m or d does not evenly divide n do
#  Decrease the value of d by 1
#  Report d as the greatest common divisor of n and m
# Write a program that reads two positive integers from the user and uses this algorithm to determine and report their
# greatest common divisor.
print("This program calculates greatest common divisor.")
n = int(input("Please enter your first number 'n' here: "))
m = int(input("Please enter your first number 'm' here: "))
# define value of d to smallest of n and m
if n > m:
    d = m
else:
    d = n
# find common divisor by dividing n and m by d and decreasing d by 1 until find the greatest common divisor
while True:
    if m % d == 0 and n % d == 0:
        break
    else:
        d -= 1
# print out the result of computations
print("The greatest common divisor of {} and {} is {}.".format(n, m, d))
