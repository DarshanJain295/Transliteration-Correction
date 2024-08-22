import json
import nltk
from nltk.corpus import words as nltk_words
nltk.download('words')
from getLanguage import langIdentify

classifier = "classifiers/HiEn.classifier"

# Load existing dictionaries
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(json.load(file))

# Replace these paths with the actual paths to your JSON files
dict1 = load_json('Indian_words.json')
dict2 = load_json('Indian_words2.json')
dict3 = load_json('Indian_words3.json')

# Combine dictionaries into a single set
existing_indian_words = dict1.union(dict2).union(dict3)

# Load and process vol4.txt
with open("./Ramayana corpus/vol4.txt", 'r', encoding='utf-8') as file:
    vol1 = file.read()

vol1 = vol1.replace("-", " ")  # Remove hyphens
vol1 = ''.join(char for char in vol1 if char.isalpha() or char.isspace())
vol1 = vol1.split()
vol1 = list(set(vol1))

english_words = set(nltk_words.words())

def is_english_word(word):
    return word in english_words

primary_cleaned = [word for word in vol1 if not is_english_word(word)]
cle = list(set(word.lower() for word in primary_cleaned))

# Filter out words already in existing dictionaries
cle = [word for word in cle if word not in existing_indian_words]

Indian_words = []
# Sending the data in classifier word by word...
for word in cle:
    tags = langIdentify(word, classifier)
    if tags[0][0][1] == "HI":
        Indian_words.append(tags[0][0][0])

# Save new Indian words to a JSON file
with open('Indian_words4.json', 'w', encoding='utf-8') as json_file:
    json.dump(Indian_words, json_file)
