import pandas as pd
import numpy as np
import formulas as fm

# import modules



mylines = []
pattern1 = r'^(?=[A-Z]+$|^[A-Z\s]+$)(?!ACT).*'
charachters = []
pattern2 = r'^(?=[A-Z]+$|^[A-Z\s]+$)\s[a-z]*'
character_lines = dict()
myfile = open("/Users/jessicaholcomb/Documents/RichardIII.txt", 'rt')
wordsperchar = {}
substrings = ['Enter', 'Exit', 'ACT', 'SCENE', 'Exeunt', '[To', 'Re-enter', '[R']

# list variables


for line in myfile.readlines():
    line = line.rstrip()
    mylines.append(line)
myfile.close()

# with connection to source file, read through lines in the file and append to list mylines, close file


fm.listsearch(pattern1, mylines, charachters)  # formula to find pattern1 in mylist and append matches to list


uniqchars = list(np.unique(np.array(charachters)))  # remove duplicate character entries to get a list of unique values


fm.instancecount(charachters, character_lines)  # counts the instances of characters (# of lines) and add to dict.


for s in substrings:
    fm.rmvsubstring(mylines, s)

# remove non-charachter lines from mylines

new_dict = fm.linestodict(mylines, charachters, uniqchars)

# Create a new dictionary with unique characters as key, lines as value using formula that distinguishes char. from line


for k in new_dict.keys():
    word_count = 0
    for l in new_dict[k]:
        words = l.split(' ')
        word_count = word_count + len(words)
        wordsperchar[k] = word_count

# count number of words spoken per character, add to dict.


for k in character_lines.keys():
    character_lines[k] = (character_lines[k], wordsperchar[k])

# zip dictionaries for the value of k in each as tuple

df = pd.DataFrame.from_dict(character_lines, orient='index', columns=['number of lines', 'number of words'])

# create pandas dataframe, df, from dictionary

df.to_csv("RichardIII.csv", index_label='character')

# export df to csv in local folder

