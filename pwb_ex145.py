# Ex. Exercise 145: Find the Longest Word in a File. solved in 39 Lines.
# In this exercise you will create a Python program that identifies the longest word(s) in a file. Any group of
# non-white space characters as a word, even if it includes numbers or punctuation marks.
# prompt user to enter the name of the file to read and find the longest word in the file
user_file = input("Please, enter the name of your file here to read: ")
# open the provided by user file
try:
    f = open(user_file, 'r')
    # create dictionary which will contain all words found in file as keys and its occurrence as value
    file_words = {}
    # read lines from file and go through each line, splitting the line by space character and adding them to list
    lines = f.readlines()
    for line in lines:
        words = line.split()
        # go through each word stored in list and if word is not found in dictionary with words from file, add such word
        # to dictionary an decrease counter of words by one
        for word in words:
            if word in file_words:
                file_words[word] += 1
            if word not in file_words:
                file_words[word] = 1
    f.close()
    # find longest word in dictionary with words from file. longest word and its length will be stored in new variables
    max_len, longest_words, occurrence =  0, [], 0
    for word in file_words.keys():
        if len(word) > max_len:
            max_len = len(word)
    for word, number in file_words.items():
        if len(word) == max_len:
            longest_words.append(word)
            occurrence = number
    # Program output message that includes the length of the longest word, along with all of the words of that length
    # that occurred in the file.
    print("The longest word(s) in file has {} characters and is {} and it is found {} times in file."
          .format(max_len, longest_words, occurrence))

# report the problem if no such file or any errors with accessing the file
except IOError:
    print("No such file or error while accessing the file with name!!!")
