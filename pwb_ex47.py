# Exercise 47: Birth Date to Astrological Sign (47 Lines). The horoscopes commonly reported in newspapers use the
# position of the sun at the time of one’s birth to try and predict the future. This system of astrology divides the
# year into twelve zodiac signs, as outline in the table attached. Write a program that asks the user to enter his or
# her month and day of birth. Then your program should report the user’s zodiac sign as part of an output message.
print("This program defines your astrological sign." + '\n')
# Ask for user input with small addition on check of the date input
while True:
    month = str(input('Please enter the name of the month here: '))
    date = int(input('Please enter the day of the month  here: '))
    if int(date) > 31:
        continue
    if month == 'February' and date > 29:
        print('February has only up to 29 days, please enter correct value!')
        continue
    if 0 < int(date) < 32:
        date = int(date)
        break
# Define the zodiac sign
if (month == 'December' and date >= 22) or (month == 'January' and date <= 19):
    sign = 'Capricorn'
if (month == 'January' and date >= 20) or (month == 'February' and date <= 18):
    sign = 'Aquarius'
if (month == 'February' and date >= 19) or (month == 'March' and date <= 20):
    sign = 'Pisces'
if (month == 'March' and date >= 21) or (month == 'April' and date <= 19):
    sign = 'Aries'
if (month == 'April' and date >= 20) or (month == 'May' and date <= 20):
    sign = 'Taurus'
if (month == 'May' and date >= 21) or (month == 'June' and date <= 20):
    sign = 'Gemini'
if (month == 'June' and date >= 21) or (month == 'July' and date <= 22):
    sign = 'Cancer'
if (month == 'July' and date >= 22) or (month == 'August' and date <= 22):
    sign = 'Leo'
if (month == 'August' and date >= 23) or (month == 'September' and date <= 22):
    sign = 'Virgo'
if (month == 'September' and date >= 23) or (month == 'October' and date <= 22):
    sign = 'Libra'
if (month == 'October' and date >= 23) or (month == 'November' and date <= 21):
    sign = 'Scorpio'
if (month == 'November' and date >= 22) or (month == 'December' and date <= 21):
    sign = 'Sagittarius'
print('Your zodiac sign is %s.' % sign)
