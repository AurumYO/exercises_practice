# Ex 109: Perfect Numbers. Solved 35 lines.
# An integer, n, is said to be perfect when the sum of all of the proper divisors of n is equal to n. For example,
# 28 is a perfect number because its proper divisors are 1, 2, 4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28.
# Write a function that determines whether or not a positive integer is perfect. Your function will take one parameter.
# If that parameter is a perfect number then your function will return true. Otherwise it will return false.
# In addition, write a main program that uses your function to identify and display all of the perfect numbers between 1
# and 10,000. Import your solution to Exercise 109 when completing this task.
from pwb_ex109 import proper_divisors


# This function fins all perfect numbers for given number
def perfect_number(number):
    # get list of all proper divisors for number by calling function proper_divisors and pass number as its argument
    proper_divisors_list = proper_divisors(number)  # get list which will contain all proper divisors for given number
    # sum will store sum af all divisors of the number by looping thorugh list of proper divisors
    divisors_sum = 0
    for p in proper_divisors_list:
        divisors_sum += p
    # if sum of all proper divisors equal to the number, function return True as result of the function
    if divisors_sum == number:
        return True
    # else if sum of all proper divisors not equal to the number, function return False as result of the function
    return False


# Main function prompts user to enter the positive integer, calls function from ex 109 to find all proper divisors
def main():
    print("From numbers in range from 1 to 10 000")
    for n in range(1, 10001):
        if perfect_number(n):
            print(n, 'is perfect')


main()
