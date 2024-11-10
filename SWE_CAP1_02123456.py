##########################
#https://github.com/ncdrakpa/SWA_CAP_Dzo_Spell_Checker
#Ngawang Choki Drakpa
#A
#02240351
##########################
#ChatGPT, youtube,
#https://chatgpt.com/, https://youtu.be/e7sX3nHjZ5Y?si=z-x5vLHpcYSHegRG, https://youtu.be/YSAn3YNuujE?si=msVwjtlVqrqKEKxK, https://youtu.be/_nkQd9SyEpw?si=0uc1VueL0qZoFl6m
#This tasked with creating a spell checker for the Dzongkha language.Of my program should read a Dzongkha text file (dzo.txt) that contains multiple spelling errors which will be provided by the tutor (refer Accessing Input File section). The program should identify and report these errors.
#https://www.youtube.com/@codingwithsagarcw
##########################
#Solution
##########################

#Read the input file

import requests
code = "https://csf101-sarver-cap1.onrender.com/get/input/351"
get_file = requests.get(code)

with open('351.txt', 'wb') as f:
    statement = f.read(get_file.content())
print("downloading 351.txt")

#check spelling

def remove_eng (infile, ofile) :
    with open (infile, "r", encoding="utf-8" ) as f:

        text = f.read ()

    text_clean = "".join ( che for che in text if ord (che) > 127 )

    with open(ofile, 'w', encoding='utf-8') as outfile:
        outfile.write(text_clean)

y = 'dictionary_converted.txt' 
x = 'clean ed_dictionary.txt'  
remove_eng ( y, x)
print (f'all characters in dictionary have removed "{y}" and  save to "{x}.')
#Main spell checking function


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


If_name_=="_main_"
import sys

if len (sys.argv)!=2:
    print("Usage: python remove_eng.py <input_file>")
    sys.exit(1)

    input_file = sys.argv[1]
    dictonary_file = "dictonary.txt"
    spell_check(input_file, dictonary_file)






































