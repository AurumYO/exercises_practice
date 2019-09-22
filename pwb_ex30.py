# Exercise 30: Units of Pressure. In this exercise you will create a program that reads a pressure from the user in
# kilo-pascals. Once the pressure has been read your program should report the equivalent pressure in pounds per
# square inch, millimeters of mercury and atmospheres. Use # your research skills to determine the conversion
# factors between these units.

print("This program accepts input of preassure in kilo-pascals and converts them to equivalents.")

# Taking input from user in kilo-pascals
press_kilopascals = float(input("Please enter the pressure in kilo-pascals: "))

# Define constants with values of conversion
KILOPASC_TO_POUNDS_PER_SQR_INCH = 0.145
KILOPASC_TO_MILLM_MERCURY = 7.501
KILOPASC_TO_ATMOSPH = 0.009869

pounds_per_inch = press_kilopascals*KILOPASC_TO_POUNDS_PER_SQR_INCH
milimiters_mercury = press_kilopascals*KILOPASC_TO_MILLM_MERCURY
atmospheres = press_kilopascals*KILOPASC_TO_ATMOSPH


# print  out equivalents in other measuring units
print("The pressure of {:0.2f} kilo-pascal is equal to {:0.4f} pounds per square inch or {:0.4f} millimeters of "
      "mercury or {:0.4f} atmospheres.".format(press_kilopascals, pounds_per_inch, milimiters_mercury, atmospheres))
