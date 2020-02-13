# Exercise 155: Gender Neutral Names (56 Lines)
print('This is the program that determines and displays all of the baby names that were used for both boys and girls'
      ' in a year specified by the user')

import os
import glob
# download set of data with baby names through years 1900-2012
folder_path = '/home/yuri/btcr/pythonworkbook_exc/BabyNames'


# function takes file name as argument, opens it, reads the data and returns the set of names from the file
def file_reader(filename):
    names = set()
    with open(filename, 'r') as f:
        lines = f.readlines()
        # loop through each line, split line by space, the name is first word in line
        for line in lines:
            text = line.split(' ')
            # add name to set with names, as it will be faster to find intersection between boys and girls names in sets
            if text[0] not in names:
                names.add(text[0])
    return names


# open *.txt files in given path with names data
files_by_year = {}
for filename in glob.glob(os.path.join(folder_path, '*.txt')):
    # file name will be last name after searched directory '..../BabyNames/'
    file_name = filename.split('/')[-1]
    # year of the data is the fist 4 digits in the begging of the name of the file followed by '_' character
    file_year = int(file_name.split('_')[0])
    # function reads each file in directory and returns set of names
    gender_names = file_reader(filename)
    # add to our dictionary with year as keys and set of names as values
    if file_year in files_by_year.keys():
        files_by_year[file_year].append(gender_names)
    else:
        files_by_year[file_year] = [gender_names]

# prompt user to enter the year to search in data for gender neutral names
user_year = int(input("Please, enter the year to find if in that year the neutral names found: "))
# check if entered by user year in data and display the result of search
if user_year not in files_by_year.keys():
    # Display an appropriate error message if in storage no data for the year requested by the user.
    print('The entered year {} is not in available data for YY1900-2012'.format(user_year))
# if entered by user year in data storage, search for year in keys and for intersection between to sets with names
# of boys and girls names
elif user_year in files_by_year.keys():
    neutral_names = files_by_year[user_year][1].intersection(files_by_year[user_year][0])
    # if in data with entered by user year found gender neutral names intersection, program reports the names
    if neutral_names:
        print('In year {} the gender neutral names were: {}.'.format(user_year, ', '.join(neutral_names)))
    # generate an appropriate message if there were no gender neutral names in the selected year.
    else:
        print("No gender neutral names were in top 100 names for year {}.".format(user_year))
