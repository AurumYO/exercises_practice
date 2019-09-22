# Ex 93: Next Prime/ solved 27 lines
# In this exercise you will create a function named nextPrime that finds and returns the first prime number larger
# than some integer, n. The value of n will be passed to the function as its only parameter. Include a main program
# that reads an integer from the user and displays the first prime number larger than the entered value. Import
# and use your solution to Exercise 92 while completing this exercise.
from pwb_ex92 import prime_definer  # import from file with Ex92 function prime_definer which defines if number is prime

# function nextPrime takes integer as argument ant returns the first prime number after this given integer
def nextPrime(n):
    search = False
    while search is False:  # loop while runs until value of search variable is True, meaning function found next prime
        res = prime_definer(n)  # we pas to module prime_definer number larger than given by user
        if res:  # if number passed to module prime_definer is prime, loop stops running  and returns prime number
            return n
        else:  # if number passed to module prime_definer is no prime
            n += 1  # number increased by 1 and goes to the next loop until the prime number found
    return n


def main():
    i = int(input("Please enter your number here: "))  # prompt user to input integer
    n = i + 1  # increasing integer by 1 due to we need to find larger prime number than inputted integer
    result = nextPrime(n)  # call function nextPrime to find irst prime number larger than some integer i
    print('The first prime number after integer {} is {}.'.format(i, result))  # display result of computations


if __name__ == '__main__':
    main()
