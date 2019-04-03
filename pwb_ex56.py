# Ex.56:

num_min = None
num_text = None
base_bill = 15
add_for_minutes = 0
add_for_text = 0
while not num_min and not num_text:
    try:
        num_min = int(input("Please enter number of air minutes used in month: "))
        num_text = int(input("Please enter number of text messages used in month: "))
    except ValueError:
        print("Entered by you numbers are not in the numbers format. Please, try again")
        continue
print("The base payment for your number amounts $15.00")

if num_min > 50:
    additional_minutes = num_min - 50
    add_for_minutes = additional_minutes * 0.25
    print("The additional charges for {0} additional air minutes is ${1:0.2f}.".format(additional_minutes,
                                                                                       round(add_for_minutes, 2)))
if num_text > 50:
    additional_text = num_text - 50
    add_for_text = additional_text * 0.15
    print("The additional charges for {0} additional text messages is ${1:0.2f}.".format(additional_text,
                                                                                         round(add_for_text, 2)))
call_support = 0.44
print("The additional charge for support of 911 call center amounts ${0:0.2f}".format(call_support))

bill = base_bill + add_for_minutes + add_for_text + call_support
tax = bill * 0.05
print("The sales tax amounts ${0:0.2f}".format(tax))
print("The amount of total bill for your phone is ${0:0.2f}.".format((bill + tax)))
