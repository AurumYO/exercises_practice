# Ex 133 Write Out Numbers in English. Solved 65 lines.


# This function takes number between 0 and 999 and displays the number in words
# Example - 142 then your function should return “one hundred forty two”
def number_to_words(num):
    # string spelled_sum will record the number in words in English
    spelled_sum = ''
    # English words corresponding to numbers stored in 3 dictionaries with names of number lower than 10, between 10
    # and 19, and in dictionary for all numbers in decimals
    simple_num = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
                  0: 'zero'}
    below_twenty = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
                    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    below_hundred = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty',
                     9: 'ninety'}
    # if the provided number is greater than 100, defined number in hundreds and remainder. name for hundred added to
    # result of the string
    if num >= 100:
        # find number in hundreds by division number by 100 and remainder from suc division
        hundreds = int(num / 100)
        remainder = num - (hundreds * 100)
        # go through dictionary with simple numbers, since number word for hundreds are the same as for simple numbers
        for k in simple_num:
            # if hundreds number same as in dictionary appends number in words to our result + word 'hundred' and space
            if k == hundreds:
                spelled_sum = simple_num[k] + ' hundred '
                # assign to number the remainder from division on 100
                num = remainder
    # if number is greater that but below 100, fin number in decimals by division by 10 and find remainder
    if num >= 20:
        decimals = int(num / 10)
        remainder = num - (decimals * 10)
        # look through dictionary with names for decimals, and find the name of the decimals and append to the result
        for k in below_hundred:
            if k == decimals:
                spelled_sum = spelled_sum + below_hundred[k] + " "
            # if remainder is greater than 0, than its value assigned to the number and further search continued
            if remainder > 0:
                num = remainder
    # if number or remainder between and 20, function searches in dictionary with numbers and equivalents for such range
    if 10 <= num < 20:
        for k in below_twenty:
            if k == num:
                spelled_sum = spelled_sum + below_twenty[k]  # and adds found words by key to result
    # if number or remainder below 10 it is searched in simple numbers dictionary for appropriate word
    if num < 10:
        for k in simple_num:
            if k == num:
                spelled_sum = spelled_sum + simple_num[k]  # and adds found words by key to result
    # function returns the number in words
    return spelled_sum


# Main function demonstrates program performance
def main():
    assert number_to_words(142) == 'one hundred forty two'
    number = int(input("Please enter your number here: "))
    # display the result of function
    print("The number {} in words is: {}.".format(number, number_to_words(number)))

if __name__ == '__main__':
    main()
