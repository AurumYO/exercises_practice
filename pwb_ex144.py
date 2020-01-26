# Exercise 144: Number the Lines in a File. solved in 23 Lines.
# Create a program that adds line numbers to a file.
# The name of the input file will be read from the user
name_file = input("Please enter the name of the file to open: ")
# as will the name of the new file that your program will create
output_file = input("Please enter the name for your output file: ")

try:
    f = open(name_file, 'r')
    output = open(output_file, 'w')
    line_number = 1
    for line in f:
        # Each line in the output file should begin with the line number, followed by a colon and a space, followed
        # by the line from the input file. After reading the line, increase the number for next line to number
        new_line = str(line_number) + ': ' + line.rstrip() + '\n'
        line_number += 1
        output.write(new_line)
    f.close(), output.close()

# raising exception if was error with accessing the file or no file found
except IOError:
    print("Error occurred while accessing the file with such name!!!")
