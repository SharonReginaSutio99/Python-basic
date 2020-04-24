"""
CP1404/CP5632 Practical
ProgammingLanguage class
Name: Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""


class ProgrammingLanguage:
    """Represent a Language object"""

    def __init__(self, name="", typing="", reflection=True, year=0):
        """Initialise a Language instance.

        name: string, reference name for language
        typing: string, either dynamic or static
        reflection: boolean, whether reflection exist in language
        year: integer, the year language is made
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return boolean value if the language is dynamically typed or not"""
        return self.typing is "Dynamic"

    def __str__(self):
        """Return a strong representation of Language object"""
        return "{}, {} Typing, Reflection={}, First appeared in {} ".format(self.name, self.typing, self.reflection,
                                                                            self.year)

    def __repr__(self):
        return "The dynamically typed languages are:\n {}".format(is_dynamic())