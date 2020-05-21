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
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            # os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    #new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = ""
    for current_index and current_letter in filename:
        new_name += current_letter

    return new_name


main()
