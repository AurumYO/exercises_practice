#Exercise 14: Height Units
#Many people think about their height in feet and inches, even in some countries that
#primarily use the metric system. Write a program that reads a number of feet from
#the user, followed by a number of inches. Once these values are read, your program
#should compute and display the equivalent number of centimeters.
#Hint: One foot is 12 inches. One inch is 2.54 centimeters.
print("MY SOLUTION")
height_feet = str(input("Enter your hight in feet here: " ))
l_height = height_feet.split('.')
feet_to_inch = int(l_height[0])*12
if len(l_height) <= 1 :
    cm = feet_to_inch * 2.54
if len(l_height) > 1 :
    height_to_inch = feet_to_inch + int(l_height[1])
    cm = height_to_inch * 2.54
print("Your height is %8.2f centimeters." % (cm))

print("SOLUTIOn FROM BOOK:")
IN_PER_FT = 12
CM_PER_IN = 2.54
print("Enter your height:")
feet = int(input("Number of feet: "))
inch = int(input("Number of inches: "))

cm = (IN_PER_FT * feet + inch) * CM_PER_IN

print("Your height in centimeters is ", cm)

