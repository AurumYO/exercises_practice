# Ex 53. Exercise 53: Assessing Employees. At a particular company, employees are rated at the end of each year.
# The rating scale begins at 0.0, with higher values indicating better performance and resulting in larger
# raises. The value awarded to an employee is either 0.0, 0.4, or 0.6 or more. Values between 0.0 and 0.4, and
# between 0.4 and 0.6 are never used. The meaning associated with each rating is shown in table. The amount of an
# employee’s raise is $2400.00 multiplied by their rating. Write a program that reads a rating from the user and
# indicates whether the performance was unacceptable, acceptable or meritorious. The amount of the employee’s raise
# should also be reported. Your program should display an appropriate error message if an invalid rating is entered.
print("This program provides the amount of raise for the employee, depending on his/her performance.")
rate = None
while not rate:
    try:
        rate = float(input("Please enter the rate for the employee (from 0.0 to 0.6): "))
    except ValueError:
        continue
if 0 <= rate < 0.4:
    performance = "Unacceptable performance"
elif 0.4 <= rate < 0.6:
    performance = "Acceptable performance"
elif rate >= 0.6:
    performance = "Meritorius performance"
upraise = 240000 * rate # calculates the upraise
print("The rate of the employee of {0} corresponds to {1} and the raise should be ${2:0.2f}."
      .format(rate, performance, upraise))
