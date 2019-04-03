# Exercise 28:Wind Chill. When the wind blows in cold weather, the air feels even colder than it actually is
# because the movement of the air increases the rate of cooling for warm objects, like people. This effect is known
# as wind chill.
# In 2001, Canada, the United Kingdom and the United States adopted the following formula for computing the wind chill
# index. Within the formula Ta is the air temperature in degrees Celsius and V is the wind speed in kilometers per hour.
# A similar formula with different constant values can be used with temperatures in degrees Fahrenheit and wind speeds
# in miles per hour.
#                    WCI = 13.12 + 0.6215Ta − 11.37V0.16 + 0.3965TaV0.16
# Write a program that begins by reading the air temperature and wind speed from the user. Once these values have
# been read your program should display the wind chill  index rounded to the closest .
# The wind chill index is only considered valid for temperatures less than or equal to 10 degrees Celsius and wind
# speeds exceeding 4.8 kilometers per hour.

print("This program calculates wind chill index (WCI).")
print()
ta = float(input("Please enter air temperature in Celsius: "))
v = float(input("Please enter wind speed in km/hour: "))

if ta <= 10 and v >= 4.8:
    wci = 13.12 + (0.6215 * ta) + (-11.37 * (v ** 0.16)) + (0.3965 * ta * (v ** 0.16))
    print("The WCI for temperature {0} and wind speed {1} is {2}.".format(ta, v, round(wci, 3)))
if ta > 10 or v < 4.8:
    print("Entered values of air temperature above 10C or wind below 4.8 km/hour therefor wci cannot be defined.")
