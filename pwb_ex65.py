# Ex 65: Compute the Perimeter of a Polygon. solved 42 lines
# Write a program that computes the perimeter of a polygon. Begin by reading the x and y values for the first point on
# the perimeter of the polygon from the user. Then continue reading pairs of x and y values until the user enters a
# blank line for the x-coordinate. Each time you read an additional coordinate you should compute the distance to the
# previous point and add it to the perimeter. When a blank line is entered for the x-coordinate your program should add
# the distance from the last point back to the first point to the perimeter. Then it should display the total perimeter.
# Sample input and output is shown below, with user input shown in bold:
# >> Enter the x part of the coordinate: 0
# >> Enter the y part of the coordinate: 0
# >> Enter the x part of the coordinate: (blank to quit): 1
# >> Enter the y part of the coordinate: 0
# >> Enter the x part of the coordinate: (blank to quit): 0
# >> Enter the y part of the coordinate: 1
# >> Enter the x part of the coordinate: (blank to quit):
#    The perimeter of that polygon is 3.414213562373095
from math import sqrt

print("This program computes the area of the polygon.")
perimeter = 0
coordinates = set()
x0 = input("Enter the x part of the cordinate: ")
y0 = input("Enter the y part of the cordinate: ")
coordinates.add((x0, y0))
xn, yn = x0, y0
# prompting  user to input coordinates until the blank line is entered and computing the perimeter
while True:
    try:
        x1 = input("Enter the x part of the cordinate (blank to quit): ")
        if x1 == '':
            x1 = x0
            break
        y1 = input("Enter the y part of the cordinate (blank to quit): ")
        if y1 == '':
            y1 = y0
            break
        else:
            dist_dot = sqrt((float(x1) - float(x0))**2+(float(y1) - float(y0))**2)
            perimeter += dist_dot
            coordinates.add((x1, y1))
            x0, y0 = x1, y1

    except ValueError:
        pass

dist_dot = sqrt((float(x1) - float(xn))**2+(float(y1) - float(yn))**2)
perimeter += dist_dot
# display the perimeter of the poligon
print("The perimetr of the polygon with coordinates {0} is {1:.3f}.".format(coordinates, perimeter))