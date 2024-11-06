##################################
# https://github.com/Zhennue/SWE-_CAPI_02240372.git

# Yeshey Zhennue
# A
# 02240372
##################################
# Chat GPT and Blackbox
# https://www.blackbox.ai/ & https://chatgpt.com/
# 1. convert docx to text.
# 2. removed english words,punctuations and numbers from dictionary (Cleaner.py).
# 3. Spelling checker (Spelling checker.py).
###################################
# SOLUTION
###################################








#Read the input file
import re
import urllib.request

def url_to_text_with_re(url):
    with urllib.request.urlopen(url) as response:
        html_content = response.read().decode('utf-8')  

    plain_text = re.sub(r'<.*?>', '', html_content)  
    plain_text = re.sub(r'\s+', ' ', plain_text).strip()

    return plain_text

url = 'https://csf101-server-cap1.onrender.com/get/input/372'
text_file = url_to_text_with_re(url)

with open('my_passage.txt', 'wb') as file:
    data = file.write(text_file.content)

print("Download my_passage.txt")







#Dictionary Cleaner
import re

def clean_english_and_symbols(input_file, output_file):
    "Remove English words, punctuation, numbers, and brackets from the Dzongkha dictionary."
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            cleaned = re.sub (r'\b[A-Za-z0-9]+\b', '', line)  
            cleaned = re.sub (r'[^\w\sཀ]', '', cleaned)  
            cleaned = re.sub (r'\s+', '', cleaned).strip()
            
            if cleaned:
                outfile.write (cleaned + '\n')

input_file = 'dictionary_file.txt' 
output_file = 'cleaned_dzongkha_dictionary.txt'  

clean_english_and_symbols(input_file, output_file)
print(f"English words, punctuation, numbers, and brackets have been removed. Cleaned file saved as {output_file}.")







#Main Spell Checking function
import re

import re
import difflib

def load_dictionary(file_path):
    """Load the dictionary from a file and return a set of lowercase words."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(word.strip().lower() for word in file)

def find_misspelled_words(line, line_number, dictionary):
    """Find and return misspelled words from a given line in the passage."""
    words = re.findall(r'\b\w+\b', line.lower()) 
    misspelled = []
    
    for position, word in enumerate(words, start=1):
        if word not in dictionary:
            misspelled.append((line_number, position, word))
    
    return misspelled

def suggest_corrections(word, dictionary):
    """Suggest the closest word matches from the dictionary for a misspelled word."""
    matches = difflib.get_close_matches(word, dictionary, n=1, cutoff=0.8)
    if matches:
        return matches[0]
    return None

def check_spelling(file_path, dictionary):
    """Check the spelling in a file and return a list of misspelled words with their line and position."""
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    misspelled_words = []

    for line_number, line in enumerate(lines, start=1):
        misspelled_words.extend(find_misspelled_words(line, line_number, dictionary))
    
    return misspelled_words

def display_results(misspelled_words, dictionary):
    """Display the misspelled words along with their line number, position, and suggested corrections."""
    if misspelled_words:
        for line_number, position, word in misspelled_words:
            correction = suggest_corrections(word, dictionary)
            if correction:
                print(f"Line {line_number}, Position {position}: Misspelled word: '{word}' -> Suggested correction: '{correction}'")
            else:
                print(f"Line {line_number}, Position {position}: Misspelled word: '{word}' -> No suggestions found")
    else:
        print("No misspelled words found.")

def main(dictionary_file, passage_file):
    dictionary = load_dictionary(dictionary_file)
    
    misspelled_words = check_spelling(passage_file, dictionary)

    display_results(misspelled_words, dictionary)

if __name__ == "__main__":
    dictionary_file = 'cleaned_dzongkha_dictionary.txt'
    passage_file = 'my_passage.txt'
    
    main(dictionary_file, passage_file)