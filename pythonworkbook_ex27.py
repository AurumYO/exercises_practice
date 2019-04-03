# Exercise 27: Body Mass Index. Write a program that computes the body mass index (BMI) of an individual. Your
# program should begin by reading a height and weight from the user. Then it should use one of the following two
# formulas to compute the BMI before displaying it. If you read the height in inches and the weight in pounds then
# body mass index is computed using the following formula:
#                                            BMI = (weight/(height × height) ) × 703
# If you read the height in meters and the weight in kilograms then body mass index is computed using this slightly
# simpler formula:
#                                     BMI = weight/(height × height)

print("This program computes BMI (Body Mass Index).")
print()
inp_user = str(input("Pres 'y' if you would like to make measures input in inches and pounds:"))
print(type(inp_user), type('y'))
if inp_user == 'y':
    height_user = float(input("Please enter your height in inches: "))
    weight_user = float(input("Please enter your weight in pounds: "))
    bmi_user = (weight_user/(height_user*height_user))*703
    print("Your BMI equals to {}".format(round(bmi_user, 2)))
else:
    inp_user_kg = str(input("Pres 'y' if you would like to make measures input in meters and kilograms:"))
    if inp_user_kg == 'y':
        height_user = float(input("Please enter your height in meters: "))
        weight_user = float(input("Please enter your height in kilograms: "))
        bmi_user = (weight_user / (height_user * height_user)) * 703
        print("Your BMI equals to {}".format(round(bmi_user, 2)))
    else:
        print("Than decide what you want and come back later.")
