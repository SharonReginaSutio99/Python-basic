"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
Name: Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""


def main():
    MENU = """
    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            f = celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(f))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            c = fahrenheit_to_celsius(fahrenheit)
            print("Result: {:.2f} C".format(c))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit"""
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius"""
    return 5 / 9 * (fahrenheit - 32)


main()
