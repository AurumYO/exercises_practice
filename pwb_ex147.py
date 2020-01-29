# Ex. 147 Words that Occur Most. Solved in 37 lines.
print('This program that displays the word (or words) that occur most frequently in a file.')
# program begins by reading the name of the file from the user, opens the file and reads all lines.
user_file = input("Please enter the name of your file to read: ")
f = open(user_file, 'r')
words_list = []
lines = f.readlines()
for line in lines:
    # program should ignore capitalization, so  it makes everything lowercase
    line = line.lower()
    # find the word(s) by splitting each line in the file at each space
    words = line.split(' ')
    for word in words:
        # any leading or trailing punctuation marks should be removed from each word.
        word = word.strip('""\':;,.!?-')
        if word != '\n':
            words_list.append(word)
words_dict = {}
for word in words_list:
    if word in words_dict.keys():
        words_dict[word] += 1
    if word not in words_dict.keys():
        words_dict[word] = 1
# loop through the dictionary with words as keys and their occurrence as values
# find most common word where value is the biggest
most_occurred_word = ''
most_common_numb = 0
for k, v in words_dict.items():
    if v > most_common_numb:
        most_common_numb = v
for k, v in words_dict.items():
    if v == most_common_numb:
        most_occurred_word = most_occurred_word + k
# display most common word in file and the number of its occurrence in file
print("The most common word(s) in file is: '{}'; in file it is occurred {} times.".format(most_occurred_word,
                                                                                             most_common_numb))
