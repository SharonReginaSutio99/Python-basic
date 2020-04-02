"""
Name: Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """"Print asterisks according to password length"""
    asterisk_count = ""
    for character in password:
        asterisk_count += "*"
    print(asterisk_count)


def get_password():
    """Get password"""
    password = input("Enter password ")
    minimum_word_count = 1
    while len(password) < minimum_word_count:
        password = input("Enter password")
    return password


main()
