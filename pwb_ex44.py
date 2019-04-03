# Exercise 44: Date to Holiday Name. Canada has three national holidays which fall on the same dates each year.
# Holiday: New year’s day - January 1; Canada day - July 1; Christmas day - December 25.
# Write a program that reads a month and day from the user. If the month and day match one of the holidays listed
# previously then your program should display the holiday’s name. Otherwise your program should indicate that
# the entered month and day do not correspond to a fixed-date holiday.
print("This program will tell if the date is holiday in Canada.")

# define dictionary with keys as number of month and values as name of the months
months = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July',
          '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
# define dictionary of Canada's holidays names as keys and value are dates represented as tuples
holidays = {'New year’s day': ('January', '01'), 'Canada day': ('July', '01'), 'Christmas day': ('December', '25')}
# prompt user to input the month
month = str(input("Please enter the month: "))
# Check if entered by user value of month is valid
if month in months.values():
    month = month
elif month in months.keys():
    month = months.get(month)
else:
    print("The value you have entered is not a month.")
    quit()
# prompt user to enter the day
day = str(input("Please enter the day of the month here: "))
if day.isdigit() and len(day) == 1:
    day = '0'+ day
elif int(day) > 31:
    print("The date you have entered is not a date!")
date = (month, day)
# define if date is holiday or not
for holiday_name, holiday in holidays.items():
    if holiday == date:
        print(f"The {month}, {day} is {holiday_name} and is official holiday in Canada!")
if date not in holidays.values():
    print(f"The {month}, {day} is not a official holiday in Canada.")
