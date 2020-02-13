# Ex. 154: Names that Reached Number One (Solved—50 Lines)
import os
import glob
# program that reads every file in the data set. Baby names data set consists of over 200 files. Each file contains
# a list of 100 names, along with the number of times each name was used. There are two files for each year:
# one containing names used for girls and the other containing names used for boys.
folder_path = '/home/yuri/btcr/pythonworkbook_exc/BabyNames'


# functions takes list of names and their occurrence from file and returns the most common name
def most_popular(list_names):
    names = {}
    for name in list_names:
        name_and_occurre = name.split(' ')
        names[name_and_occurre[0]] = int(name_and_occurre[1])
    most_common = 0
    for k, v in names.items():
        if most_common < v:
            most_popular_name = k
            most_common = v
    return most_popular_name


# most popular names stored in two lists, which should not include any repeated values.
boys_names, girls_names = [], []
for filename in glob.glob(os.path.join(folder_path, '*txt')):
    if 'Girls' in filename:
        with open(filename, 'r') as girls_text:
            girl_names_year = girls_text.readlines()
            girls_text.close()
            # find most common name using function most_popular()
            number_one_name = most_popular(girl_names_year)
            if number_one_name not in girls_names:
                girls_names.append(number_one_name)
    if 'Boys' in filename:
        with open(filename, 'r') as boys_text:
            boys_names_year = boys_text.readlines()
            boys_text.close()
            number_one_name = most_popular(boys_names_year)
            if number_one_name not in boys_names:
                boys_names.append(number_one_name)

# Display the most popular names for boys and the other containing the most popular names for girls.
print("The most popular boy names that reached Number One are: ")
for name in boys_names:
    print(name)
print("The most popular girls names that reached Number One are: ")
for name in girls_names:
    print(name)
