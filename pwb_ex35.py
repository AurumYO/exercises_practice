# Exercise 35: Dog Years. It is commonly said that one human year is equivalent to 7 dog years. However this simple
# conversion fails to recognize that dogs reach adulthood in approximately two years. As a result, some people believe
# that it is better to count each of the first two human years as 10.5 dog years, and then count each additional human
# year as 4 dog years. Write a program that implements the conversion from human years to dog years described in the
# previous paragraph. Ensure that your program works correctly for conversions of less than two human years and for
# conversions of two or more human years. Your program should display an appropriate error message if the user enters
# a negative number.

print("This program converts human years to dog's years.")

# Ask for human years input from user
hum_years = float((input("Enter the human years number: ")))
while hum_years <= 0:
    print("Entered value of human years is equal or less than 0 or not a number!")
    hum_years = float((input("Enter the human years number: ")))

# defining conversion values as constants
FIRST_HUMTODOG_YEARS = 10.5
REST_HUMTODOG_YEARS = 4

# Make conversion of the human years to dog years
if hum_years <= 21:
    dog_years = round(hum_years / FIRST_HUMTODOG_YEARS, 1)
elif hum_years > 21:
    dog_years = 2 + (hum_years - 21) * REST_HUMTODOG_YEARS

# Print outcome of the conversion
print(f"The {hum_years} human years is equal to {dog_years} dog years.")
