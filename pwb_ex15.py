#Exercise 15: Distance Units
#In this exercise, you will create a program that begins by reading a measurement
#in feet from the user. Then your program should display the equivalent distance in
#inches, yards and miles. Use the Internet to look up the necessary conversion factors
#if you don’t have them memorized.
feet = float(input("Enter the distance in fees: "))
inch = feet * 12
yard = feet * 0.333333
mile = feet * 0.00018939
print("%5d feet is equal to %8.2f inches, or to %8.4f yards, or to %8.8f miles." % (feet, inch, yard, mile), sep='')
