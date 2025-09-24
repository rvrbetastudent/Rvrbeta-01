"""
===========================================================
Program Name: MadLibsProgram.py
Author: Ryan Vrbeta
Date: 1995-08-07
Description:
    This program performs some Mad Libs that read in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB OR VERB appears in the text file.
    It is designed to use input and file reading to output some fun Mad Libs.
===========================================================
"""

import re
import os

# List of placeholder words to be replaced in the template
PLACEHOLDERS = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']

def prompt_replacement(word: str) -> str:
    """
    Prompts the user to enter a replacement for the given placeholder word.
    Adds 'a' or 'an' as appropriate before the prompt.
    """
    article = 'an' if word[0] in 'AEIOU' else 'a'
    return input(f"Enter {article} {word.lower()}: ")

def mad_libs(filename: str) -> None:
    """
    Reads the template file, replaces placeholders with user input,
    and prints the completed Mad Libs story.
    """
    # Get the directory where the script is located and build the full file path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    with open(file_path, 'r') as file:
        text = file.read()

    # Compile a regex pattern to match any placeholder word
    pattern = re.compile('|'.join(PLACEHOLDERS))

    # Function to use for each regex match, prompting the user for input
    def replacer(match):
        return prompt_replacement(match.group())

    # Replace all placeholders in the text with user input
    result = pattern.sub(replacer, text)

    # Output the final Mad Libs story
    print("\nYour Mad Libs story:")
    print(result)

if __name__ == "__main__":
    # Prompt the user for the template filename and run the Mad Libs program
    filename = input("Enter the name of the Mad Libs template file: ")
    try:
        mad_libs(filename)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found in the current directory.")
    except Exception as e:
        print(f"An error occurred: {e}")
