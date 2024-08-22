from getLanguage import langIdentify
classifier ="classifiers/HiEn.classifier"

import nltk
from nltk.corpus import words as nltk_words
nltk.download('words') 
english_words = set(nltk_words.words())

with open("./Ramayana corpus/vol4.txt", 'r',encoding = 'utf-8') as file:
        vol1 = file.read()

vol1 =  vol1.replace("-", " ")  # Remove hyphens
vol1 = ''.join(char for char in vol1 if char.isalpha() or char.isspace())
vol1 = vol1.split()
vol1 = list(set(vol1))

def is_english_word(word):
    return word in english_words
primary_cleaned = [word for word in vol1 if not is_english_word(word)]

cle =list(set(word.lower() for word in primary_cleaned ))

Indian_words=[]
# sending the data in classifier word by word...
for word in cle:
    tags= langIdentify(word, classifier)
    if(tags[0][0][1]=="HI"):
        Indian_words.append(tags[0][0][0])

import json
with open('Indian_words4.json', 'w',encoding='utf-8') as json_file:
    json.dump(Indian_words, json_file)
