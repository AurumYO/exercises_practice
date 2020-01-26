# Ex. 143: Concatenate Multiple Files. solved in 27 lines.

# Prompt user to enter the names of the files to concatenate or blank line to finish input of files's names
user_file = input("Please enter the name for your file to read it or blank line to stop: ")
files_list = []
while user_file != '':
    files_list.append(user_file)
    user_file = input("Please enter the name for your file to read it or blank line to stop: ")

# Display an appropriate error message if your program is started without any command line parameters.
if len(files_list) <= 0:
    print("No files to read!!!")
# program reads each file provided by user
for n in range(len(files_list)):
    # opens the file, and if programs is able to access the file with such name it reads the file
    try:
        f = open(files_list[n], 'r')
        # The files are displayed in the same order that they appear on the command line.
        for line in f:
            line.rstrip()
            print(line, end='')
        # close file after we red and displayed it
        f.close()
    # It should generate an error message for any file that cannot be displayed, and then proceed to the next file.
    except IOError:
        print("No such file or error while accessing the file with name!!!")
