"""
CP1404/CP5632 Practical
Client code use of Guitar class
Name: Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""

from prac_06.guitar import Guitar


def main():
    """Make a list of guitars."""
    guitars = []
    print("My guitars")

    loop = True
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    while loop:
        guitar_name = input("Name: ")
        if guitar_name != "":
            guitar_year = int(input("Year: "))
            guitar_cost = float(input("Cost: "))
            guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
        else:
            loop = False

    format_printing(guitars)


def format_printing(guitars):
    """Format printing structure."""

    print("... snip...")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                  vintage_string))


main()
