"""
CP1404/CP5632 Practical
Sort files into subdirectories for each extension part 1
Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""

import os
import shutil


def main():
    """Sort files into subdirectories for each extension."""
    # Confirm starting directory
    print("Starting Directory is: {}".format(os.getcwd()))

    # Change to FilesToSort directory
    os.chdir("FilesToSort")

    # Loop through each file in the current directory
    for filename in os.listdir("."):
        # Separate file name to obtain extensions
        split_name = filename.split(".")

        # Make new directories for new extensions
        try:
            os.mkdir(split_name[-1])
        except FileExistsError:
            pass

        # Move files to correct extension folders
        shutil.move(filename, split_name[-1]+'/')


main()
