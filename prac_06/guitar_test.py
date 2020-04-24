"""CP1404/CP5632 Practical - Client code to use the Guitar class.
Name: Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals"""

from prac_06.guitar import Guitar


def main():
    """Test to use Guitar class"""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 123678.30)
    print(gibson)
    print("{} get_age() - Expected 98. Got {}".format(gibson.name, gibson.get_age()))
    print("{} get_age() - Expected 7. Got {}".format(another_guitar.name, another_guitar.get_age()))
    print("{} is_vintage() - Expected True. Got {}".format(gibson.name, gibson.is_vintage()))
    print("{} is_vintage() - Expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))
main()
