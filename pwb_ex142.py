# Exercise 142: Display the Tail of a File. Solved 35 lines.

# define the limit for number of last lines to display
lines_limit = 10

# prompt user to name the file to be open and red
try:
    user_file = input("Please enter the name of your file to read: ")
    f = open(user_file, 'r')
    # empty list will store separate lines from file
    last_lines = []
    # program loops through the file and strips empty spaces in the beginning of the sentence
    for line in f:
        line.rstrip()
        # and appends the line to the list with separate lines from file
        last_lines.append(line)
        # when list with lines from file exceeds the number of last lines to show program will delete the first
        # line in list, emptying space in list with lines in that way the length of list with line not exceeds 10 lines
        if len(last_lines) > lines_limit:
            last_lines.pop(0)
    # close file after the program read it through all lines
    f.close()

    # program goes through list with left 10 lines from file left after whole file was red and displays them
    for line in last_lines:
        print(line, end='')

# Display an appropriate error message if the file requested by the user does not exist
# or if the command line parameter is omitted.
except IOError:
    print("The error occurred while accessing the file with such name!!!")
    quit()
