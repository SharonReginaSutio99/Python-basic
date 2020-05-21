"""
CP1404/CP5632 Practical
Clean inconsistent file names
Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""

import os


def main():
    """Clean inconsistent song lyrics file names."""

    # Change to desired directory
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        # print("Directory:", directory_name)
        # print("\tcontains subdirectories:", subdirectories)
        # print("\tand files:", filenames)
        # print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:

            new_name1 = get_separate_words(filename)
            print(new_name1)
            #print("Renaming {} to {}".format(filename, new_name2))

            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name1)
            # os.rename(full_name, new_name)


def get_separate_words(filename):
    """Separate name when next letter is uppercase."""
    new_name = ""
    special_character = "_()"
    # Go through letter one by one
    for current_index, letter in enumerate(filename):
        new_name += letter

        # Check the next letter and stop before last letter
        if current_index < len(filename) - 1:
            if letter not in special_character and filename[current_index + 1] not in special_character:
                # Add a _ to separate names if next letter is uppercase
                if letter.isalnum and filename[current_index + 1].isupper():
                    new_name += "."

    return new_name


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()
