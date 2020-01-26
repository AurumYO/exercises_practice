# Exercise 129: Two Dice Simulation (Solved—42 Lines)
#In this exercise you will simulate 1,000 rolls of two dice. Sample output is below:
# Total      Simulated percentage           Expected percentage
#  2                 2.90                         2.78


# function that simulates rolling a pair of six-sided dice. Function will not take any parameters.
# It returns the total that was rolled on two dice as its only result
def dice_roll():
    from random import randint
    x, y = randint(1, 6), randint(1, 6)
    return x + y


# Main program that uses dice_roll function to simulate rolling two six-sided dice 1,000 times.
# It counts the number of times that each total occurs. Then it should display a table that summarizes this data.
# Express the frequency for each total as  a percentage of the total number of rolls.
# Your program should also display the percentage expected by probability theory for each total
def main():
    total_rols = 1000
    # dictionary expected percentage will contain dice sum as key and percentage of expected total dice roll
    expected_percentage = {2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33,
                           11: 5.56, 12: 2.78}
    # dictionary simulated_percentage will contain dice sum as key and percentage of simulated total dice roll
    simulated_percentage = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    # this loop rolls dices 1000 times and counts how many times each total sum got in simulation
    for n in range(total_rols):
        spin = dice_roll()
        simulated_percentage[spin] = simulated_percentage[spin] + 1
    # this loop updates simulated total dice roll dictionary values from number of times total encountered to percentage
    for k, v in simulated_percentage.items():
        simulated_percentage[k] = round((v/total_rols * 100), 2)
    # display output of the program in readable format
    print('{:<8}{:<25}{:<8}'.format('Total', 'Simulated percentage', 'Expected percentage'))
    for k, v in simulated_percentage.items():
        print("{:<8}{:<25} {:<8}".format(k, simulated_percentage[k], expected_percentage[k]))


if __name__ == '__main__':
    main()
