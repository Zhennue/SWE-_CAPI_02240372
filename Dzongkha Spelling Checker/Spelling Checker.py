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