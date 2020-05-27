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
            fixed_name = get_fixed_filename(filename)
            new_name = get_separate_words(fixed_name)
            capitalized_name = capitalize_title(new_name)
            print("Renaming {} to {}".format(filename, capitalized_name))

            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, capitalized_name)
            os.rename(full_name, new_name)


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
                # Add a _ to separate names without spaces if next letter is uppercase
                if letter.isalnum and filename[current_index + 1].isupper():
                    new_name += "_"

    return new_name


def capitalize_title(new_name):
    """Capitalize titles properly."""
    capitalized_name = ""
    # Go through letter one by one
    for current_index, letter in enumerate(new_name):
        # Check the next letter and stop before last letter
        if current_index < len(new_name) - 1:
            if letter.islower() and new_name[current_index - 1] == "_":
                # Upper case correctly according to title.
                capitalized_name += letter.upper()
            else:
                capitalized_name += letter
    capitalized_name += "t"
    return capitalized_name


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()
