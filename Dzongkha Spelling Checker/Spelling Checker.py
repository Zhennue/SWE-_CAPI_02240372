import re

def load_dictionary(file_path):
    with open (file_path, 'r', encoding='utf-8') as file:
        return set (word.strip().lower() for word in file)

def find_misspelled_words(line, line_number, dictionary):
    words = re.findall (r'\b\w+\b', line.lower())
    misspelled = []
    
    for position, word in enumerate(words, start=1):
        if word not in dictionary:
            misspelled.append((line_number, position, word))
    
    return misspelled

def check_spelling(file_path, dictionary):
    with open (file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    misspelled_words = []

    for line_number, line in enumerate (lines, start=1):
        misspelled_words.extend (find_misspelled_words(line, line_number, dictionary))
    
    return misspelled_words

def display_results(misspelled_words):
    """Display misspelled words with their line and position."""
    if misspelled_words:
        for line_number, position, word in misspelled_words:
            print(f"Line {line_number}, Position {position}: Misspelled word: '{word}'")
    else:
        print("No misspelled words found.")

def main(dictionary_file, passage_file):
    dictionary = load_dictionary(dictionary_file)
    misspelled_words = check_spelling(passage_file, dictionary)
    display_results(misspelled_words)

dictionary_file = 'cleaned_dzongkha_dictionary.txt' 
passage_file = 'my_passage.txt' 

main(dictionary_file, passage_file)