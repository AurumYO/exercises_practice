# Ex 68: Parity Bits. solved 25 lines
print("This program computes the bits.")
line_len = input("Please enter 8 bites: ")

while line_len != "":
    if line_len.count('0') + line_len.count('1') != 8 or len(line_len) != 8:
        print("That wasn't 8 bits ... Try again.")
    else:
        ones = line_len.count('1')
        if ones % 2 == 0:
            print("The parity bit should be 0.")
        else:
            print("The parity bit should be 1.")
    line_len = input("Please enter 8 bites: ")
