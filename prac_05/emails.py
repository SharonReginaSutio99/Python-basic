"""
CP1404/CP5632 Practical
Store user's emails and names
Name: Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""


def get_name(email):
    full_name = email.split("@")
    name = full_name.split(".")
    for i in range(len(name)):
        name[i] = name[i].title()
    full_name = ','.join(name)
    print(full_name)


def main():
    email = input("Email: ")
    get_name(email)


main()



