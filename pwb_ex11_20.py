##Ex11: Fuel Efficiency. In US, fuel efficiency for vehicles is expressed in miles-pergallon (MPG).
## In Canada, fuel efficiency is expressed in liters-per-hundred kilometers (L/100 km).
## determine how to convert from MPG to L/100 km. Then create a program that reads a value from the user in US
## units and displays the equivalent fuel efficiency in Canadian units.
#eff_mpg = float(input("Please enter fuel efficiency in miles-per-gallon (MPG) here: "))
#us_gallon = 3.785411784
#mile = 1.609344
#liters_100km = (100*us_gallon)/(mile*eff_mpg)
#print("The fuel efficiency for vehicles of {0:1.2f} MPG is equivalent of {1:1.2f} L/100 km."
#      .format(eff_mpg, liters_100km))

##Ex12: Distance Between Two Points on Earth. The surface of the Earth is curved, and the distance between degrees of longitude
##varies with latitude. As a result, finding the distance between two points on the surface
##of the Earth is more complicated than simply using the Pythagorean theorem.
##Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s surface.
## The distance between these points, following the surface of the Earth, in kilometers is:
##  distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))
##Create a program that allows the user to enter the latitude and longitude of two points on the Earth in degrees.
## Your program should display the distance between the points, following the surface of the earth, in kilometers.
import math
t1,g1 = map(int,input("Please enter the latitude and longtitude of the point A separating by space: ").split())
t2,g2 = map(int,input("Please enter the latitude and longtitude of the point B separating by space: ").split())
delta_g1g2 = g1 - g2
distance_deg = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(delta_g1g2))
dist_km = math.radians(distance_deg)
print("The distance between the points A and B, following the surface of the earth is {0:1.1f} kilometers.".format(dist_km))

