"""
CP1404/CP5632 Practical
Sort files into categories user wants for each extension
Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""

import os


def main():
    """Sort files into categories user wants."""
    extension_to_category = {}
    # Change to FileToSort directory
    os.chdir("FilesToSort")

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        extension = filename.split(".")[-1]
        if extension not in extension_to_category:
            category = input("What category would you like to sort {} files into?".format(extension))
            extension_to_category[extension] = category
        print(extension_to_category.items())
        # In case user put in existing folder
        try:
            os.mkdir(category)
        except FileExistsError:
            pass

        # Move files to directories based on categories by renaming
        os.rename(filename, "{}/{}".format(extension_to_category[extension], filename))


main()
