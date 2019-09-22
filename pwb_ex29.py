# Exercise 29: Celsius to Fahrenheit and Kelvin. Write a program that begins by reading a temperature from the user
# in degrees Celsius. Then your program should display the equivalent temperature in degrees Fahrenheit and
# degrees Kelvin. The calculations needed to convert between different units of temperature to be found on internet.

print("This program reads temperature in Celsius from user and converts it to Fahrenheit and Kelvin.")

# Taking input from user of the temperature in Celsius
temper_Celsius = float(input("Please enter the temperature in Celsius: "))

# Conversion form Celsius to Fahrenheit done by formula
temper_Fahren = (temper_Celsius * 9/5) + 32

# Conversion form Celsius to Kelvin done by formula
temper_Kelvin = temper_Celsius + 273.5

# Showing output of the program
print("The temperature of {0} degrees Celsius is equal to {1} degrees Fahrenheight or {2} degrees Kelvin."
      .format(temper_Celsius, temper_Fahren, temper_Kelvin))
