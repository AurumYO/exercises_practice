# Exercise 86: The Twelve days of Christmas. solved 48 lines.  Your task is to write a program that displays the
# complete lyrics for The Twelve Days of Christmas. Write a function that takes the verse number as its only parameter
# and displays the specified verse of the song. Call that function 12 times with integers that increase from 1 to 12.

integers_orders = {1: 'first', 2: 'second', 3: 'third', 4: 'forth', 5: 'fifth', 6: 'sixth', 7: 'seventh', 8: 'eighth',
                   9: 'ninth', 10: 'tenth', 11: 'eleventh', 12: 'twelve'}


def song_verses(n):
    day = integers_orders[n]
    print('On the {} day of Christmas'.format(day))
    print('my true love sent to me:')

    if n > 11:
        print('12 drummers drumming')
    if n > 10:
        print('11 pipers piping')
    if n > 9:
        print('10 lords a-leaping')
    if n > 8:
        print('Nine ladies dancing')
    if n > 7:
        print('Eight maids a-milking')
    if n > 6:
        print('Seven swans a-swimming')
    if n > 5:
        print('Six geese a-laying')
    if n > 4:
        print('Five golden rings')
    if n > 3:
        print('Four calling birds')
    if n > 2:
        print('Three french hens')
    if n > 1:
        print('Two turtle doves, and')
    if n > 0:
        print('A partridge in a pear tree')

    print()


def main():
    for n in range(1, 13):
        song_verses(n)


main()
