# Exercise 150: Remove Comments. Solved in 46 lines.

# Program prompts user to enter the name of the input file and the name for output file
user_file = input("Please, enter the name of your Python source file here: ")
output_file_name = input("Please enter the name for the output file: ") + '.py'

# program tries to open file entered by user, and performs search of 3 character in the beginning of each line
# if comment character is not is not found in the beginning than such line saved to output file
try:
    f = open(user_file, 'r')
    lines = f.readlines()
    # create new file of name entered by user with modified file will be saved
    output_file = open(output_file_name, 'w')
    # Check each line in the file to determine if a # character is present.
    # cases where the comment character occurs inside of a string is ignored
    for line in lines:
        # ignore lines which starts directly from # character
        if not line.startswith('#'):
            # strip spaces in lines which might me indented and store line in new variable
            new_line = line.lstrip(' ')
            # if the first character in line with removed spaces at the beginning is not searched # character
            # than original line not starts with # and program writes to our output file original line
            if not new_line.startswith('#'):
                print(line)
                #
                output_file.write(line)
    # close original file and save the modified file using a new name that was entered by the user
    f.close(), output_file.close()

# The program displays an appropriate error message if a problem is encountered while accessing the files.
except IOError:
    print("No such file or error while accessing the file with name!!!")
