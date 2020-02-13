# Exercise 157: Distinct Names (41 Lines)


# this function read files
def extract_names_from_file(filename):
    with open(filename, 'r') as f:
        text = f.readlines()
        f.close()
        names_set = set()
        for line in text:
            line = line.split(' ')
            if line[0] not in names_set:
                names_set.add(line[0])
    return names_set


# main function reads every file in the baby names data. Program outputs two lists: one witch contains all girls names
# second with boys names. Neither of lists should contain any repeated values.
def main():
    import os
    import glob
    # report what program does and download set of data with baby names through years 1900-2012
    print('This program determines which names were used most often within a time period.')
    folder_path = '/home/yuri/btcr/pythonworkbook_exc/BabyNames'
    # track that each name used for a boy and each name used for a girl.
    girls_names, boys_names = set(), set()
    for filename in glob.glob(os.path.join(folder_path, '*.txt')):
        # file name will be last name after searched directory '..../BabyNames/'
        file_name = filename.split('/')[-1]
        # gender contained in the ned of the file's name, after the '_' character
        gender = file_name.split('_')[1]
        if 'Girls' in gender:
            names_girls_filedata = extract_names_from_file(filename)
            # set with all girls names updated with names from current file
            girls_names.update(names_girls_filedata)
        if 'Boys' in gender:
            names_boys_filedata = extract_names_from_file(filename)
            # set with all boys names updated with names from current file
            boys_names.update(names_boys_filedata)
    # convert sets with boys and girls names to list with non repetitive names of boys and girls in each list
    list_girls, list_boys = list(girls_names), list(boys_names)
    print('Girls non-repetitive names are: \n', list_girls)
    print('Boys non-repetitive names are: \n', list_boys)


if __name__ == '__main__':
    main()
