# Exercise 156: Most Births in a given Time Period (76 Lines)


# this function reads provided file with such name and returns dictionary with names as values
# and their occurrence as values
def file_reader(filename):
    names = dict()
    with open(filename, 'r') as f:
        lines = f.readlines()
        # loop through each line, split line by space, the name is first word in line
        for line in lines:
            text = line.split(' ')
            # add name to dictionary with names ad kes and their occurrence eas values
            if text[0] not in names:
                names[text[0]] = int(text[1])
        f.close()
    return names


# this program updates the dictionary with names data with new data from new file and returns updated total data
def update_names_dictionary(all_names, current_names):
    for name, quantity in current_names.items():
        if name in all_names.keys():
            all_names[name] += quantity
        else:
            all_names[name] = quantity
    return all_names


# this function takes dictionary with names and their occurrence and returns most common name
def most_common_name(names_dict):
    most_common = 0
    for k, v in names_dict.items():
        if most_common < v:
            most_popular_name = k
            most_common = v
    return most_popular_name


def main():
    import os
    import glob
    # report what program does and download set of data with baby names through years 1900-2012
    print('This program determines which names were used most often within a time period.')
    folder_path = '/home/yuri/btcr/pythonworkbook_exc/BabyNames'

    # prompt user to supply the first and last years of the range to analyze.
    start = int(input("Please, enter the first year of range from which to start names data exploration: "))
    end = int(input("Please, enter the last year of range to finish names data exploration: "))

    # open *.txt files in given path with names data
    girls_names, boys_names = dict(), {}
    for filename in glob.glob(os.path.join(folder_path, '*.txt')):
        # file name will be last name after searched directory '..../BabyNames/'
        file_name = filename.split('/')[-1]
        # year of the data is the fist 4 digits in the begging of the name of the file followed by '_' character
        file_year = int(file_name.split('_')[0])
        gender = file_name.split('_')[1]
        if start <= file_year <= end and 'Girls' in gender:
            girls = file_reader(filename)
            girls_names = update_names_dictionary(girls_names, girls)
        if start <= file_year <= end and 'Boys' in gender:
            boys = file_reader(filename)
            boys_names = update_names_dictionary(boys_names, boys)

    # Display the boy’s name and the girl’s name given to the most children during the indicated years.
    print('Name {} was given most commonly to girls during YY{}-{}.'.format(most_common_name(girls_names), start, end))
    print('Name {} was given most commonly to boys during YY{}-{}.'.format(most_common_name(boys_names), start, end))


if __name__ == '__main__':
    main()
