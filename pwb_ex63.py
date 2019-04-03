# Ex 63: Write a program that displays a temperature conversion table for degrees Celsius and
# degrees Fahrenheit. The table should include rows for all temperatures between 0
# and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate
# headings on your columns. The formula for converting between degrees Celsius and
# degrees Fahrenheit can be found on the internet.

from prettytable import PrettyTable

print("This table shows the Celcius degrees and their equivalent in Fahrenheit.")

cel = [x for x in range(0, 101) if x % 10 == 0]

t = PrettyTable(['Celcius', 'Fahrenheit'])

for x in cel:
    t.add_row([x, x * 9 / 5 + 32])

print(t)