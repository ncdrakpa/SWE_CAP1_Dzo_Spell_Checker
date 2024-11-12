import os

def main():
    while True:
        dictionary_path = input("Enter the Dzongkha dictionary file path: ")
        text_path = input("Enter the text file path to spell check: ")

        #  paths
        if not os.path.isfile(dictionary_path):
            print("Dictionary file path is invalid. Please try again.")
            continue
        if not os.path.isfile(text_path):
            print("Text file path is invalid. Please try again.")
            continue

        # spell-checking paths are valid
        incorrect_words = spell_check(dictionary_path, text_path)
        if incorrect_words:
            print("Misspelled words found:")
            for word in incorrect_words:
                print(word)
        else:
            print("No spelling errors found!")
        break

def load_dictionary(dict_path):
    # Load words from the dictionary file to access
    with open(dict_path, 'r', encoding='utf-8') as file:
        return {line.strip() for line in file}

def spell_check(dict_path, text_path):
    dictionary_words = load_dictionary(dict_path)
    misspelled = []

    # Open and read the text file, checking each word
    with open(text_path, 'r', encoding='utf-8') as file:
        for line in file:
            for word in line.split():
                if word not in dictionary_words:
                    misspelled.append(word)
    
    return misspelled

if __name__ == '__main__':
    main()
