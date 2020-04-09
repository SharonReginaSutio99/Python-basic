"""
CP1404/CP5632 Practical
Data file -> lists program
Name: Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    for index in data:
        print("{} is taught by {} and has {} students".format(index[0], index[1], index[2]))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    compiled_lists = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2]) # Make the number an integer (ignore PyCharm's warning)
        compiled_lists.append(parts)
    return compiled_lists
    input_file.close()


main()