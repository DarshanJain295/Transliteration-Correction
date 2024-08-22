import json
import re

# Load the dictionary from the JSON file
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)

my_dict1 = load_json('dictionary.json')
# my_dict2 = load_json('dict2.json')
# my_dict3 = load_json('dict3.json')
# my_dict4 = load_json('dict4.json')

# Merge all dictionaries into a single dictionary
my_dict = {}
for dictionary in [
    my_dict1,  # First dictionary
    # my_dict2,  # Commented out
    # my_dict3,  # Commented out
    # my_dict4   # Commented out
]:
    my_dict.update(dictionary)

# Function to replace words while maintaining capitalization
def replace_words(text, replacement_dict):
    words = re.findall(r'\b\w+\b|\W', text)  # Using regular expression to find words and special characters
    replaced_words = []
    for word in words:
        if word.isalnum():  # Check if word is alphanumeric
            original_word = word
            if word.endswith(','):  # Check if word ends with comma
                word = word[:-1]  # Remove comma
            lowercase_word = word.lower()
            if lowercase_word in replacement_dict:
                if original_word.istitle():  # Check if original word is capitalized
                    replaced_word = replacement_dict[lowercase_word].capitalize()
                elif original_word.isupper():  # Check if original word is fully capitalized
                    replaced_word = replacement_dict[lowercase_word].upper()
                else:
                    replaced_word = replacement_dict[lowercase_word]
                if original_word.endswith(','):  # Add comma back if original word had it
                    replaced_word += ','
                replaced_words.append(replaced_word)
            else:
                replaced_words.append(original_word)
        else:
            replaced_words.append(word)  # Keep special characters intact
    return ''.join(replaced_words)

# Read the original text file
with open('./Ramayana corpus/vol4.txt', 'r', encoding='utf-8') as file:
    original_text = file.read()

# Replace words in the original text
modified_text = replace_words(original_text, my_dict)

# Write the modified text to a new file or overwrite the original file
with open('modified_text4.txt', 'w', encoding='utf-8') as file:
    file.write(modified_text)
