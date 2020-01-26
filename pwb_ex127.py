# Ex 127: The Sieve of Eratosthenes (Solved—33 Lines)
#The Sieve of Eratosthenes is a technique that was developed more than 2,000 years ago to easily find all of the
# prime numbers between 2 and some limit, say 100.
# Create a Python program that uses this algorithm to display all of the prime numbers between 2 and a limit entered
# by the user. If you implement the algorithm correctly you should be able to display all of the prime numbers less than 1,000,000
# in a few seconds.


# this function returns the list of only prime numbers between 2 and user's upper limit
# In function used algorithm which is provided in the book, which however is slow at large lists of numbers
def only_primes(limit):
    numbers_list, primes_list = [], []
    # Write down all of the numbers from 0 to the limit. Cross out 0 and 1 because they are not prime. Set p equal to 2
    numbers_list = [n for n in range(limit + 1)]
    p = 2
    # While p is less than the limit do
    while p < limit:
        # Cross out all multiples of p (but not p itself)
        for n in range(len(numbers_list)):
            if numbers_list[n] % p == 0 and numbers_list[n] > p:
                numbers_list[n] = 0
        numbers_list = [n for n in numbers_list if n > 0]
        # print(numbers_list, 'xer')
        # Set p equal to the next number in the list that is not crossed out
        for n in numbers_list:
            if n > p:
                p = n
                break
        limit = numbers_list[-1]
    print(numbers_list[-1])

    # generate result as all prime numbers greater than 2
    primes_list = [n for n in numbers_list if n >= 2]
    # Report all of the numbers that have not been crossed out as prime
    return primes_list


# this function takes upper limit from user and displays all prime numbers from 2 to user's limit
def main():
    print("This program displays the list of only prime numbers between 2 and user's upper limit.")
    limit = int(input("Please enter your limit for prime numbers display: "))
    primes = only_primes(limit)
    print("Prime numbers are: ", primes)



if __name__ == '__main__':
    main()


# much more simpler is following using set data structure
def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes


print(primes_sieve(13))
