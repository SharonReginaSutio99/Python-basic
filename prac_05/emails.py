"""
CP1404/CP5632 Practical
Store user's emails and names.
Name: Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""


def get_name(email):
    """Separate name from email."""
    possible_name = email.split("@")[0]
    full_name = ""
    names = possible_name.split(".")
    for name in names:
        full_name += name.title() + " "
    full_name = verify_name_input(full_name)
    return full_name


def verify_name_input(full_name):
    """Filter unwanted name input."""
    name_confirmation = input("Is your name {}? (Y / N)".format(full_name))
    name_confirmation_input = ["", "y", "n"]
    while name_confirmation.lower() not in name_confirmation_input:
        print("Invalid input")
        name_confirmation = input("Is your name {}? (Y / N)".format(full_name))
    else:
        if name_confirmation.lower() == "" or name_confirmation.lower() == "y":
            full_name = full_name
        else:
            full_name = input("Name: ")
    return full_name


def main():
    """Store user's name and emails."""
    emails_to_names = {}
    email = input("Email: ")
    while email != "":
        full_name = get_name(email)
        emails_to_names[email] = full_name
        email = input("Email: ")
    for email, name in emails_to_names.items():
        print("{} ({})".format(name, email))


main()
