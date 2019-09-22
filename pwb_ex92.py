# Exercise 92: Is a Number Prime? Solved - 28 lines
# A prime number is an integer greater than 1 that is only divisible by one and itself. Write a function that determines
# whether or not its parameter is prime, returning True if it is, and False otherwise. Write a main program that reads
# an integer from the user and displays a message indicating whether or not it is prime. Ensure that the main program
# will not run if the file containing your solution is imported into another program.


# function returns True if provided number > 1  and divisible by 1 and itself meaning that number is prime
def prime_definer(number):
    counter = 0  # counter will be counting how many numbers give zero division on given to function number
    if number > 1:
        for n in range(1, number+1):  # we take all numbers 'n' greater than 1 and <= to make division on given number
            if number % n == 0:  # if remainder from division of given number by n gives zero
                counter += 1  # we increase counter by one
        if counter < 3:  # if number is divided only by two numbers than functions returns True, meaning it is prime
            return True
    else:  # else our number is not prime and function returns False
        return False


def main():
    number = int(input('Please, enter your number here: '))  # ask for number input from user
    res = prime_definer(number)  # given by user number passed to the function
    if res is True:  # if output of function is True, meaning that the given by user number is prime
        print("The number you have provided {} is prime number.".format(number))
    else:  # if output of function is False, than given by user number is not prime
        print("The number you have provided {} is not prime number.".format(number))


if __name__ == '__main__':
    main()
