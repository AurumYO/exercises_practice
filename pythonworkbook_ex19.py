# Create a program that determines how quickly an object is traveling when it hits the ground.
# The user will enter the height from which the object is dropped in meters (m). Because the object is dropped
# its initial speed is 0m/s. Assume that the acceleration due to gravity is 9.8m/s2. You can use the formula
# V(f)=sqrt(V(i)2+2ad) to compute the fin.speed, (v(f)), when initial speed(V(i), acceleration (a), distance(d) known.
import math

a = 9.8  # acceleration due to gravity is 9.8m/s2
print("This program calculates how quickly an object is traveling when it hits the ground")

# this line prompting user to enter the height which is distance in our formula
d = float(input("Please, enter the height from which object is falling in meters: "))

v = math.sqrt(2*a*d)

print('The object is traveling to the ground ', round(v, 4), 'milliseconds.')

print('The object is traveling to the ground %.4f milliseconds.' % v)
