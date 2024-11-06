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
-⁠dzongkha_spell_checker.py
Set: For storing unique reference words from the cleaned dictionary for fast lookup.
List: For holding words extracted from each line of the input file during iteration.
String: For handling and processing the lines read from the input file.

-⁠txt conveter.py
Strings: For storing file names and the content extracted from the .docx file.

-⁠txt downloader.py
Strings: For storing the URL and the text content of the HTTP response.

-cleaner.py
Strings: For storing file names and the content of each line from the input file.




## Algorithms
1.Loading the Dictionary (load_dictionary)
-Reads a dictionary file, where each word is assumed to be on a new line.
-Converts all words to lowercase to make the spelling check case-insensitive.
-Stores the words in a set, which allows for O(1) lookup time when checking for misspelled words.

2.Finding Misspelled Words (find_misspelled_words)
-Uses re.findall to extract all the words from a line using the regex pattern r'\b\w+\b'. This pattern matches word boundaries (\b) and sequences of word characters (\w+), effectively splitting the line into words.
-Converts each word to lowercase for case-insensitive comparison.
-For each word, checks if it exists in the dictionary:
-If not, appends a tuple containing the line number, position, and the misspelled word to the misspelled list.

3.Checking the Entire Passage (check_spelling)
-Reads the passage file line by line.
-Calls find_misspelled_words for each line, storing all misspelled words with their line numbers and positions.

4.Displaying Results (display_results)
-If any misspelled words are found, it prints the line number, word position, and the misspelled word.
-If no misspelled words are found, it prints "No misspelled words found."



## Performance Analysis
1. load_dictionary Function
Performance: The load_dictionary function reads a file line by line and adds each word (after stripping and lowering the case) into a set.
Complexity: O(n), where n is the number of words in the dictionary file. Sets provide O(1) time complexity for lookups, so loading the dictionary is efficient.

2. find_misspelled_words Function
Performance: Regular expressions are powerful but can be costly in terms of performance for large texts. The complexity depends on the size of the line and the pattern. Generally, re.findall is O(m) where m is the length of the line, but regex can take longer based on the complexity of the expression.

3. check_spelling Function
Performance:
The function reads all lines of the file into memory using file.readlines(), which has a time complexity of O(n) where n is the number of lines in the file.

4. re.findall and Its Impact
re.findall(r'\b\w+\b', line.lower()):
This regular expression is efficient for finding word boundaries. However, if the text contains many non-alphanumeric characters, the performance can degrade slightly because the engine needs to evaluate the boundaries for every character in the string.
In typical use cases with moderate text sizes, this performance impact is usually negligible. But for very large files, this could become a bottleneck.

5. Displaying Results
The display_results function simply iterates through the list of misspelled words and prints them.
Performance: If there are k misspelled words, the complexity is O(k), but this is typically very fast.




## Challenges and Solutions
1.Python did not read request so i changed the code using def 
2.Linking the dictionary and passage was not working but by making it variable and using main function it worked (main(dictionary_file, passage_file)




## Future Improvements
1.Word's AutoCorrect feature is useful for checking spelling and grammar. When Word indicates a word in a document with a squiggle that it may be misspelt or incorrect, you can right-click the word to see suggestions.



## References
1.(Docx to text converter) - https://www.youtube.com/watch?v=Mi3j54ZMxOc
2.(English word cleaner) - https://www.youtube.com/watch?v=hhjn4HVEdy0
3.(Spelling checker) - https://www.youtube.com/watch?v=_nkQd9SyEpw
4.(Algorithms of spelling checker) - https://www.youtube.com/watch?v=d-Eq6x1yssU
