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