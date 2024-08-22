from ai4bharat.transliteration import XlitEngine
e = XlitEngine("hi", beam_width=10, rescore=True)

from aksharamukha import transliterate
def translit(text):
    # using XlitEngine to get the closest correct word in Hindi.
    out = e.translit_word(text, topk=5)
    return out['hi'][0]
def to_iso_indic_15919(text):
    # Transliterating Devanagari script to ISO Indic 15919
    iso_text = transliterate.process('devanagari', 'iso', text)
    return iso_text

import json
with open('Indian_words4.json', 'r') as json_file:
    indian_words = json.load(json_file)

transliterations = {}
for word in indian_words:
    temp = translit(word)
    new = to_iso_indic_15919(temp)
    transliterations[word] = new

with open('dict4.json', 'w',encoding='utf-8') as json_file:
    json.dump(transliterations, json_file,ensure_ascii=False)