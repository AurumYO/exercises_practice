# Exercise 24: Units of Time
# Create a program that reads a duration from the user as a number of days, hours, minutes, and seconds.
# Compute and display the total number of seconds represented by this duration.

print("This program computes the total number of seconds by inputed duration.")

# prompting to input number of days, converting to seconds
# by multiplying by 24 hours/day and 60 min per hour and 60 sec per minute
days_to_seconds = int(input("Please, enter number of days: ")) * 24 * 60 * 60

# prompting to input number of hours, converting to seconds
# by multiplying by  60 min per hour and 60 sec per minute
hours_tp_seconds = int(input("Please, enter number of hours: ")) * 60 * 60

# prompting to input number of minutes, converting to seconds
# by multiplying 60 sec per minute
minutes_to_seconds = int(input("Please, enter number of minutes: ")) * 60

# prompting to input number of seconds
seconds = int(input("Please, enter number of seconds: "))

# calculating total number of seconds by summing user inputs transferred to seconds
total_seconds = days_to_seconds + hours_tp_seconds + minutes_to_seconds + seconds

# printing out the result of computations
print("The total number of seconds in %d days %d hours %d minutes and %d seconds is %d seconds in total!" %
      (days_to_seconds, hours_tp_seconds, minutes_to_seconds, seconds, total_seconds))
