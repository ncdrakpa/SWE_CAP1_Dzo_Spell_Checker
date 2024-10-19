# Dzongkha Spell Checker 
## Project Overview

## Table Of contents

-[usage](#usage)
-[Implementations](#implementations-details)
-[Data Structure](#data-structures)
-[Algorithms](#algorithms)
-[challenges and Solution](#Challners-and-Solution)
-[Future Improvements](#future-improvements)
-[References](#references)
 
 ## Usage 
TO use the Dzongkha 
To explain how to use the Dzongkha Spell Checker implemented in Python, I'll provide a guide on command-line arguments, expected input/output formats, and a basic usage example.

Usage Guide for Dzongkha Spell Checker
Command-Line Usage

You can use the Dzongkha Spell Checker by running it from the command line. The program will take a Dzongkha text file or string as input, check for spelling mistakes, and output the corrected version of the text, along with suggestions for potential spelling errors.

## 3 Command-Line Arguments:
--input (Required):
Path to the input Dzongkha text file that needs to be spell-checked.

--output (Optional):
 Provide's the corrected text and  will be printed to the terminal.

--mode (Optional):
The spell checker mode. This can be one of the following:

simple: Simple spell-checking, only highlights errors.

The number of spelling correction suggestions to be displayed for each error in interactive mode.

### Input/Output Format

Input Format:
The input should be a Dzongkha text file. Provide
with a path to a .txt file to input a raw Dzongkha string when invoking the script.

The file is to be encoded in UTF-8 to support Dzongkha characters properly.

Output Format:
The spell checker will output the corrected Dzongkha text, along with suggestions for any detected errors.

If no output file is specified, the output will be printed to the console. Otherwise, it will be saved to the file provided in the --output argument.

## Implementation Details


The structure of the code provided focuses on removing non-Dzongkha (non-Unicode) characters, such as English alphabet characters, from a text file. Below is a detailed breakdown of the code structure and the key implementation decisions:

<b>Code Structure
1. remove_eng() Function:
<ul>
<li>Purpose: This function reads an input file, filters out non-Dzongkha (non-Unicode) characters (specifically, characters with an ASCII value less than or equal to 127), and writes the cleaned result to an output file.

<li>Parameters:
infile: The name/path of the input file containing the original text (likely with English characters).

<li>ofile: The name/path of the output file where the cleaned text will be saved.
</ul>

2. Opening Input File:

with open(infile, 'r', encoding='utf-8') as f:
<ul>
<li>The input file is opened using the utf-8 encoding to handle Dzongkha (and other Unicode) characters properly.

<li>The use of with ensures that the file is properly closed after reading, even if an error occurs.
Reading and Cleaning the Text:
</ul>

3. Reading and Cleaning the Text:

ext = f.read()
text_clean = ''.join(char for char in text if ord(char) > 127)
 <ul >
<LI>The entire file content is read into a string, text.

<li>The expression ord(char) > 127 filters out characters with an ASCII value of 127 or below (which includes standard English characters and punctuation). This retains only Unicode characters like Dzongkha.

<li>The ''.join() method constructs a new string text_clean containing only the non-ASCII characters.
</ul>

4. Writing Cleaned Text to Output File:

with open(ofile, 'w', encoding='utf-8') as outfile:
    outfile.write(text_clean)
 <ul>
 <li>The cleaned text is written to the output file using utf-8 encoding to maintain the integrity of the remaining Unicode characters (Dzongkha or any others).
</ul>
 5. Main Code Execution:

y = 'dictionary_converted.txt'
x = 'cleaned_dictionary.txt'
remove_eng(y, x)
<ul>
<li>The main code defines two variables:
<li>y is the name of the input file.
<li>x is the name of the output file.
<li>The remove_eng() function is called with y and x as arguments, cleaning the input file and saving the result to the output file.
</li>
</ul>

6. Completion Message:

print(f"all characters in dictionary have removed '{y}' and save to '{x}'.")

<ul>
<li>This print statement provides feedback to the user, confirming that the process is complete and indicating the input and output files involved</ul>

## Data Structures

The main data structure used in this code is a string, which holds the text read from the input file and the cleaned text after processing. Strings in Python are a built-in sequence type that efficiently handle text data and are ideal for this task.

1. A string is used because:
<ul>
<li>
It allows easy filtering and joining of characters.

<li>It efficiently handles Unicode, which is essential for Dzongkha.

<li>String operations like join() make the code cleaner and more readable.</ul>


2. A list is used because:
<ul>
 <li>Lists are mutable, allowing for in-place changes. This can be more efficient when performing multiple operations on the text, such as spell corrections.

<li>If the text needed to be processed in multiple passes.

 (e.g., once for filtering characters, and once for spelling correction), lists would be better suited for such operations.
</ul>

3. A dictonary is used because:
<ul>
<li>While the current code only removes English characters, a dictionary could be useful for storing a set of predefined corrections or rules for spell-checking.

<li>For example, the dictionary could map commonly misspelled Dzongkha words to their correct forms. 
</ul>

## Algorithms

In a Dzongkha spell checker, the core algorithms focus on tasks like efficient dictionary lookup and cleaning of non-relevant characters (e.g., non-Dzongkha characters).If I  break down the key algorithms  context and their relevance to the code I provided and the overall structure of a spell checker.

1. Dictionary Lookup:

Dictionary lookup is crucial for determining whether a word is correctly spelled. Dzongkha words need to be compared against a predefined list (or dictionary) of valid words.

2. Text Cleaning:
   
Cleaning the text involves removing irrelevant characters (such as English letters or punctuation) and ensuring that the input consists only of valid Dzongkha text. In the provided code, this is done using a simple filter algorithm.

## Performance Analysis
Provide an analysis of your solution's time and space complexity. Include any performance optimizations you implemented,

The time complexity of the spell checker would be O(n), where n is the length of the input text. This is because the spell checker reads the input text character by character, and the time complexity of each operation (such as checking if a character is valid Dzongkha, or looking up a word in a dictionary) is constant.

 It does not contain any actual code for the spell checker functionality. However, I can provide an analysis of the time and space complexity for a hypothetical Dzongkha spell checker that follows the structure and algorithms described.

 The space complexity of the spell checker would also be O(n), as it reads the entire input text into memory before processing it. This is necessary because the spell checker needs to have the entire input text available in order to perform its operations.

In conclusion, the time and space complexity of a Dzongkha spell checker that follows the structure and algorithms described in the guide would be O(n) for both time and space complexity. To optimize the performance of the spell checker, we could consider implementing a trie data structure for dictionary lookups and using a streaming algorithm to process the input text.

## Challenges and Solutions

Main challenges I have encountered during the development of the Dzongkha spell checker:

1. Handling Dzongkha Script and Unicode Characters

Challenge: 

Dzongkha is written in a complex script, which is composed of multiple Unicode characters. Ensuring that the system handles Unicode characters properly was challenging, especially when distinguishing between Dzongkha and other characters, such as English letters.

Solution:

The key is using utf-8 encoding consistently when reading and writing files.
The ord() function is used to filter out characters based on their Unicode values (ASCII characters have values <= 127, whereas Dzongkha characters have higher Unicode values). This allows for easy filtering and processing of the text.
File those containing Dzongkha text, are opened with utf-8 encoding to prevent errors or data loss during read/write operations.

 2. Performance with Large Text Files
    
Challenge:

 Processing large text files, especially with Dzongkha script, caresult in performance issues as text processing often requires multiple passes through the data.

Solution: 

Optimizing the algorithm: By filtering out non-Dzongkha characters in a single pass using list comprehensions, the performance is enhanced without using extra memory

3. challenges faced with the code :

Challenge:

Alternative use of different code made the performance worse.

Solution:

Trouhgh the help of youtube videos and withe the help of AI
and friends have been provided me more infromation regarding the code and hepled me to over coem this issue.

 Code Challenges that i have faced, Solutions:

<table border="1" cellpadding="10" cellspacing="0">
  <thead>
    <tr>
      <th>Challenge</th>
      <th>Solution</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Accurate removal of non-Dzongkha characters</td>
      <td>Use Dzongkha-specific Unicode ranges to filter characters.</td>
    </tr>
    <tr>
      <td>File encoding issues</td>
      <td>Use utf-8 encoding when reading and writing files to handle Dzongkha script properly.</td>
    </tr>
    <tr>
      <td>Lack of robustness for edge cases</td>
      <td>Implement checks for numbers, punctuation, and mixed-language text.</td>
    </tr>
    <tr>
      <td>Performance with large files</td>
      <td>Process text line-by-line or in chunks to avoid memory issues with large files.</td>
    </tr>
    <tr>
      <td>Basic error handling</td>
      <td>Add error handling for file access, encoding issues, and unexpected inputs.</td>
    </tr>
    <tr>
      <td>Limited functionality (no spell-checking)</td>
      <td>Implement spell-checking by integrating a dictionary and checking word validity.</td>
    </tr>
    <tr>
      <td>Lack of feedback or output summary</td>
      <td>Provide feedback on the number of characters removed, and other useful output information.</td>
    </tr>
  </tbody>
</table>

## Future Improvements
1. Dzongkha is a morphologically rich language with complex word structures. A future improvement could include the ability to handle morphologically derived words, where the spell checker understands various forms of the same word (e.g., verbs, nouns with prefixes and suffixes).

2. Use machine learning models for predictive text or error detection, where the spell checker can learn from user input and adapt to new or frequently used words.

3. Many documents in Dzongkha might include English words or other languages. Future versions of the spell checker could detect and correctly handle mixed-language documents, allowing English words to pass while only checking Dzongkha for spelling error

## Refrences

1. [Resources 1 Youtube](https://youtu.be/_nkQd9SyEpw?si=LoOMOrTNL8-RM2bV)
2. [Resources 2 Youtube](https://youtu.be/2SSr-RVAwIg?si=p445v7wXNTV2y6f9)
3. [Resources 3 geeksforgeeks](https://www.geeksforgeeks.org/)


