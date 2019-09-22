# Exercise 25: Units of Time (Again)
# In this exercise you will reverse the process described in the previous exercise. Develop a program that begins by
# reading a number of seconds from the user. Then your program should display the equivalent amount of time in
# the form D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds respectively.
# The hours, minutes and seconds should all be formatted so that they occupy exactly two digits,
# with a leading 0 displayed if necessary.

print("This program transfers number of seconds in D:HH:MM:SS format.")
print()
seconds_total = int(input("Please enter your total amount of seconds: "))

days = seconds_total // 86400
remainder = seconds_total - (days * 86400)
hours = remainder // 3600
remainder -= (hours * 3600)
minutes = remainder // 60
remainder -= (minutes * 60)
seconds = remainder
print("The entered equivalent of time is %d:%02d:%02d:%02d ." % (days, hours, minutes, seconds))

# # Alternative solution / solution from book
# seconds_per_day = 86400
# seconds_per_hour = 3600
# seconds_per_minute = 60
#
# seconds_total = int(input("Please enter your total amount of seconds: "))
#
# days = seconds_total / seconds_per_day
# remainder = seconds_total % seconds_per_day
# hours = remainder / seconds_per_hour
# remainder = remainder % seconds_per_hour
# minutes = remainder / seconds_per_minute
# seconds = remainder % seconds_per_minute
# print("The entered equivalent of time is %d:%02d:%02d:%02d ." % (days,hours,minutes,seconds))