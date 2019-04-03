print("This table shows off the discount table for the variety of goods.")

purchases = [4.95, 9.95, 14.95, 19.95, 24.95]

for i in purchases:
    org_price = "$" + str(i)
    disc = i * 0.6
    discount = '$' + str(round(disc, 2))
    new_price = "$" + str(round((i - disc), 2))
    print("Original price: {}, Discount: {}, New price: {} ".format(org_price, discount, new_price))

# solution using prettytable
print()
print("Solution with prettytable library")
from prettytable import PrettyTable

tab = PrettyTable(['Original price', 'Discount', 'New price'])

for x in purchases:
    disc = round((x * 0.6), 2)
    new_prc = round(x - (x * 0.6), 2)
    tab.add_row([x, disc, new_prc])
print(tab)
