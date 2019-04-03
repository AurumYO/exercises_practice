# Ex 55. Radiation frequency.
print("This program defines the light depending on the radiation frequency.")
radio_freq = None
while not radio_freq:
    try:
        radio_freq = int(input("Please enter the radiation frequency: "))
    except ValueError:
        print("The radiation frequency should be an integer. Try again")
        continue
# Define the radiation frequency of the input
if radio_freq < (3 * 10 ** 9):
    wave = "Radio waves"
elif (3 * 10 ** 9) >= radio_freq < (3 * 10 ** 12):
    wave = "Microwaves"
elif (3 * 10 ** 12) >= radio_freq < (3 * 10 ** 14):
    wave = "Infrared light"
elif (3 * 10 ** 14) >= radio_freq < (7.5 * 10 ** 14):
    wave = "Visible light"
elif (7.5 * 10 ** 14) >= radio_freq < (3 * 10 ** 17):
    wave = "Ultraviolet light"
elif (3 * 10 ** 17) >= radio_freq < (3 * 10 ** 19):
    wave = "X-rays"
elif radio_freq >= (3 * 10 ** 17):
    wave = "Gamma rays"
radio_freq = int(radio_freq / 1000000)
print("The radiation frequency of {0}MHz corresponds to {1}.".format(radio_freq, wave))
