# Ex54. Exercise 54: Wavelengths of Visible Light. The wavelength of visible light ranges from 380 to 750 nanometers
# (nm). While the # spectrum is continuous, it is often divided into 6 colors. Write a program that reads a wavelength
# from the user and reports its color. Display an appropriate error message if the wavelength entered by the user is
# outside of the visible spectrum.
wave_len = None
while not wave_len:
    try:
        user_len = int(input("Please enter the wavelength to ge the color (in range of visible light "
                             "ranges from 380 to 750 nm): "))
        if user_len in range(380, 751):
            wave_len = user_len
    except ValueError:
        print("The entered value is out of visible light ranges from 380 to 750 nm. Try again")
        continue
if 379 < wave_len <= 449:
    color = "Violet"
elif 450 <= wave_len <= 494:
    color = "Blue"
elif 495 <= wave_len <= 569:
    color = "Green"
elif 570 <= wave_len <= 589:
    color = "Yellow"
elif 590 <= wave_len <= 619:
    color = "Orange"
elif 620 <= wave_len <= 750:
    color = "Red"
print("The light's wavelength of {0} corresponds to {1} color.".format(wave_len, color))

