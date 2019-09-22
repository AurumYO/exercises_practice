# Exercise 20: Ideal Gas Law. The ideal gas law is a mathematical approximation of the behavior of gasses as
# pressure, volume and temperature change. It is usually stated as:
#                  PV = nRT
# where P is the pressure in Pascals, V is the volume in liters, n is the amount of substance in moles,
# R is the ideal gas constant, equal to 8.314 J/mol K , and T is the temperature in degrees Kelvin.
# Write a program that computes the amount of gas in moles when the user supplies the pressure, volume and temperature.
# Test your program by determining the number of moles of gas in a SCUBA tank. A typical SCUBA tank holds 12 liters
# of gas at a pressure of 20,000,000 Pascals (approximately 3,000 PSI). Room temperature is approx. 20C or 68F.
# Hint: A temperature is converted from Celsius to Kelvin by adding 273.15 to it. To convert a temperature
# from F to Kelvin, deduct 32 from it, multiply it by 59 and then add 273.15 to it.

r = 8.314

pressure = int(input("Please enter the pressure in Pascals: "))
volume = int(input("Please enter the volume in liters: "))
room_celsius_temperature = float(input("Please enter the room temperature in Celsius: "))

# transfering room temperature from Celsius to Kalvin
temp_kelvin = room_celsius_temperature + 273.15

# calculate the amount of substance in moles
num_moles = (r * temp_kelvin)/(pressure * volume)

print("The amount of substance in tank is %.4f moles" % num_moles)

