# Exercise 141: Display the Head of a File. solved 40 lines.
#It displays the first 10 lines of a file whose name is provided as a command line parameter.
# Display an appropriate error message if the file requested by user does not exist or if the command line
# parameter is omitted.

lines_number = 10

try:
    # open file for reading
    user_file = input("Please enter your file name in '.txt' format here: ")
    f = open(user_file, 'r')
    # read each line in the file
    line = f.readline()
    # set counter with value 0
    counter = 0
    # in loop read 10 lilnes in file or until blank line in file
    while counter < lines_number:
        # strip spaces in line
        line.rstrip()
        # counting lines by increasing the counter
        counter = counter + 1
        # print the line
        print(line, end='')
        # read next line in file
        line = f.readline()
    # close the file after reading 10 lines
    f.close()
# raising exception if was error with accessing the file or no file found
except IOError:
    print("En error occurred while accessing the file.")
