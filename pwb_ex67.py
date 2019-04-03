# Ex 67: Admission Price. solved in 38 lines
# A particular zoo determines the price of admission based on the age of the guest. Guests 2 years of age and less are
# admitted without charge. Children between 3 and 12 years of age cost $14.00. Seniors aged 65 years and over cost
# $18.00. Admission for all other guests is $23.00.
# Create a program that begins by reading the ages of all of the guests in a group from the user, with one age entered
# on each line. The user will enter a blank line to indicate that there are no more guests in the group. Then your
# program should display the admission cost for the group with an appropriate message. The cost should be displayed
# using two decimal places.

print("This program computes the total price for group admitting the zoo.")
total_price = 0

while True:
    person_age = input("Enter the age of person from the visitor's group (or blank to finish): ")
    if person_age == '':
        break
    elif int(person_age) <= 2:
        total_price += 0
    elif int(person_age) >= 65:
        total_price += 18
    elif 3 >= int(person_age) <= 12:
        total_price += 14
    else:
        total_price += 23.00

# outprint the results of computations
print("The total amount due to payment from the group amounts {0:.2f}$.".format(total_price))
