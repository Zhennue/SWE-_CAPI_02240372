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
1. Set - Dictionary Data Structure
Purpose: The set is used to store the dictionary of valid words.

Why Chosen:
Fast Lookup: The set in Python offers O(1) average time complexity for membership testing (i.e., checking if a word exists in the dictionary). This is crucial for spelling checking, as we need to quickly verify whether a word is valid or misspelled.

Uniqueness: A set automatically ensures that there are no duplicate words in the dictionary, which simplifies the process.

Case Insensitivity: The dictionary is stored in lowercase, allowing case-insensitive comparison with the words in the passage.

Example:
dictionary = {"འབྱུང", "གུང", "འཕུང", "དོན", "ཞིང", "བཟོ"}


2. List - Passage Data Structure
Purpose: The list is used to store the lines of text from the passage that will be checked for spelling errors.

Why Chosen:
Order Preservation: A list preserves the order of the lines and words, which is essential for reporting the position of misspelled words in the passage.

Efficient Iteration: It allows for easy iteration over the lines (or words) of the passage. Each line can be processed independently, checking for misspelled words in sequence.

Simplicity: A list is a simple and effective way to store multiple lines of text that need to be processed one by one.

Example:
passage = [
    "དོན་ལུས་དགོས་པའི་འདོད་ཡོངས",
    "འདོགས་འཕུང་།",
    "ཞིང་བཟོ་ལས་དང་གསོལ"
]


3. List of Tuples - Misspelled Words
Purpose: The list of tuples stores information about the misspelled words found in the passage. Each tuple contains the line number, word position, and the misspelled word itself.

Why Chosen:
Organized Data: The tuple stores multiple related pieces of information together (line number, word position, misspelled word). This is an efficient way to keep track of misspelled words along with their context.

Readability: Using a list allows for easy collection of all misspelled words across the passage. The tuples provide a clear structure to store the detailed information about the misspelled word.

Indexing: The list can be easily iterated to report each misspelled word along with its exact location (line and position).

Example:
misspelled_words = [
    (2, 1, "དད"),
    (3, 2, "དོད")
]


4. Dictionary - Suggested Corrections
Purpose: The dictionary (in Python) is used to store suggested corrections for each misspelled word. The key is the misspelled word, and the value is the suggested correct word.

Why Chosen:
Fast Lookup for Suggestions: Like the dictionary, the suggested corrections are stored in a dictionary for fast lookup. This allows you to quickly retrieve the most appropriate correction for each misspelled word.

Easy Mapping: The key-value structure of a dictionary allows for a clear mapping between the incorrect word (key) and its suggested correction (value). This is simple to manage and efficient for spell-checking tasks.

Example:
suggested_corrections = {
    "དད": "དོད",
    "དོད": "དོན"
}


5. String - File Paths

Purpose: The string is used to represent the file paths for both the passage file and the dictionary file.

Why Chosen:
Simplicity: File paths are naturally represented as strings in Python, and this allows for easy manipulation and passing of file locations to functions.

Flexibility: By using a string, the paths can be easily modified or passed as command-line arguments, making the tool flexible for various file locations.

Example:
passage_file = "my_passage.txt"
dictionary_file = "cleaned_dzongkha_dictionary.txt"

## Algorithms
Dictionary Loading: Loads words from a dictionary file into a set for fast membership testing, ensuring case-insensitive lookups.

Passage Parsing: Reads the passage file line by line, splitting each line into words using regular expressions to handle punctuation.

Spelling Check: Compares each word in the passage to the dictionary. If a word is not found in the dictionary, it's flagged as misspelled.

Misspelled Word Tracking: Misspelled words are stored in a list of tuples, containing the line number, word position, and the word itself.

Integration: Combines dictionary loading, passage parsing, and spelling checking to display misspelled words and their locations in the passage.


## Performance Analysis

Dictionary Loading: Loading the dictionary into a set takes O(n) time, where n is the number of words in the dictionary. This is efficient due to the O(1) average time complexity for lookups in a set.

Passage Parsing: Parsing the passage line by line and extracting words using regular expressions takes O(m * k), where m is the number of lines and k is the average number of words per line.

Spelling Check: Checking each word against the dictionary is done in O(1) for each word, so the overall time complexity for spelling checks is O(m * k).


## Challenges and Solutions

1. Handling Large Files:
Challenge: Large passage or dictionary files can slow down the process.

Solution: Using sets for the dictionary ensures O(1) lookup time, making word checks faster even with large files. Additionally, processing files line by line avoids loading the entire file into memory at once.

2. Case Sensitivity:
Challenge: Spelling errors can appear due to case mismatches.

Solution: Convert both the passage words and dictionary to lowercase to perform case-insensitive comparison.

3. Punctuation and Special Characters:
Challenge: Words may include punctuation or special characters, leading to false mismatches.

Solution: Use regular expressions to extract words while ignoring punctuation, ensuring accurate word matching.

4. Accuracy of Suggestions:
Challenge: Providing accurate spelling corrections can be difficult, especially for similar-looking words.

Solution: While not implemented in full here, integrating a probabilistic spelling correction algorithm (e.g., using edit distance or machine learning models) can improve correction accuracy.

5. Encoding Issues:
Challenge: Non-standard characters (like Dzongkha) may cause encoding problems.

Solution: Use UTF-8 encoding when reading files to ensure compatibility with non-English characters.


## Future Improvements
1. Enhanced Correction Suggestions:
Implement more sophisticated spelling correction algorithms (e.g., Levenshtein distance or probabilistic models) to provide more accurate suggestions for misspelled words.

2. Support for Multiple Languages:
Extend the tool to support multi-language dictionaries, enabling the checker to work with different languages or mixed-language passages.

3. GUI or Web Interface:
Develop a Graphical User Interface (GUI) or web application to make the tool more user-friendly, allowing users to upload files and see spelling suggestions interactively.

4. Performance Optimization:
For large files, consider implementing parallel processing or streaming to process the text more efficiently, especially for dictionaries with millions of words.

5. Integration with Text Editors:
Integrate the tool with popular text editors or IDEs (e.g., VSCode, Sublime Text) for real-time spell checking as users type.


## References
1. [Download Files From a URL Using Python](https://www.youtube.com/watch?v=LyymFN9t4kw)
2. [Dictionary](https://www.youtube.com/watch?v=MZZSMaEAC2g)