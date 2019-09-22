# Ex 82: Taxi Fare. solved in 22 lines
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters traveled.
# Write a function that takes the distance traveled (in kilometers) as its only parameter and returns the total fare
# as its only result. Write a main program that demonstrates the function.
print("This program calculates the taxi fare.")
print()
# define fixed pricing of fare in variables
base_fare = 4.00
add_fare = 0.25


# this function takes miles as parameter and returns the taxi fare for riding given miles
def taxi_fare(miles):
    if miles < 140:
        return float(miles * base_fare)
    else:
        extra_fee = int(miles / 140) * add_fare
        base_fee = float(miles * base_fare)
        return round((base_fee + extra_fee), 2)


# this function asks for an input from user and displays result of computations
def main():
    user_miles = int(input("Please enter the distance of the trip in miles: "))
    fare = taxi_fare(user_miles)
    print("The taxi fare for riding {} miles is ${}.".format(user_miles, fare))


main()
