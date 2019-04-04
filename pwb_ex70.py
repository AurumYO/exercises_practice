# Ex 70: Write a program that implements a Caesar cipher. Allow the user to supply the message and the shift amount,
# and then display the shifted message. Ensure that your program encodes both uppercase and lowercase letters. Your
# program should also support negative shift values so that it can be used both to encode messages and decode messages.
print("This is the Ceasar Cipher!")
origin_message = input("Please enter your message for cipher: ")
shift = int(input("Please enter the shift value: "))
ciphered_message = ""

for l in origin_message:
    if l >= 'a' and l <= 'z':
        position = ord(l) - ord('a')
        position = (position + shift) % 26
        new_l = chr(position + ord('a'))
        ciphered_message = ciphered_message + new_l
    elif l >= 'A' and l <= 'Z':
        position = ord(l) - ord('A')
        position = (position + shift) % 26
        new_l = chr(position + ord('A'))
        ciphered_message = ciphered_message + new_l
    else:
        ciphered_message = ciphered_message + l

print("The ciphered message is:")
print(ciphered_message)
