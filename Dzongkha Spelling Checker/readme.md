# Dzo Spell Checker

## Project overview
1.It is mainly used to check and compare spelling of my passage with the dictionary (cleaned_dzongkha_dictionary.txt).
2.Used to detect incorrect words in my passage.
3.It identifies and corrects misspelled words

## Table of Contents
1.Usage
2.Implementation Details
3.Data Structures
4.Algorithms
5.Challenges and Solutions
6.Future Improvements
7.References

## Usage
1.Import regular expression(provides a set of functions to search, match, and manipulate strings using regular expressions) : import re

2.Define a function to load dictionary :  def load_dictionary(file_path):
    with open (file_path, 'r', encoding='utf-8') as file:
        return set (word.strip().lower() for word in file)

3.Define function to find misspelled words - for position check : def find_misspelled_words(line, line_number, dictionary):
    words = re.findall (r'\b\w+\b', line.lower())
    misspelled = []

4.Define function to check spelling - for line check : def check_spelling(file_path, dictionary):
    with open (file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

5.Define function to diplay results (Misspelled and no misspelled words) : def display_results(misspelled_words):
    """Display misspelled words with their line and position."""
    if misspelled_words:
        for line_number, position, word in misspelled_words:
            print(f"Line {line_number}, Position {position}: Misspelled word: '{word}'")
    else:
        print("No misspelled words found.")

6.Link dictionary and passage file : dictionary_file = 'cleaned_dzongkha_dictionary.txt' 
passage_file = 'my_passage.txt' 

7.Show the output : main(dictionary_file, passage_file)




'''bash
python Spelling Checker.py my_passage.txt
'''




## Implementation
-It scans the text and extracts the words contained in it.
-It then compares each word with a known list of correctly spelled words (i.e. a dictionary)
-An additional step is a language-dependent algorithm for handling morphology.

## Data Structures
