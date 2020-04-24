"""
CP1404/CP5632 Practical
Guitar class
Name: Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar instance.
        name: string
        year: integer
        cost: float
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of guitar object."""
        return "{} ({}): ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Return age of the guitar object."""
        return 2020 - self.year

    def is_vintage(self):
        """Return whether guitar object is vintage."""
        return self.get_age() >= 50
