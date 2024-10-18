

import string
def extract_words (text): 
    words = [word.strip (string. punctuation) .lower () for word in text.split()]
    return set (words)

with open ("351.txt", encoding="utf-8") as file:
    words1 = set ([word.strip (string. punctuation).lower () for word in file.read ().split ()])

with open ("cleaned_dictionary.txt", encoding="utf-8") as file:
    words2 = set ([word.strip (string. punctuation) .lower () for word in file. read().split ()])

unique_to_file1 = {word for word in words1 if word not in words2}

[print(f"The word '{word}' from 351.txt is incorrect.") for word in unique_to_file1]

