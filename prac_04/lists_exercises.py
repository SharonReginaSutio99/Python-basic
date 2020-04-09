"""
Name: Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""


def main():
    basic_operations()

    username_checker()


def username_checker():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    name = input("Username: ")
    if name in usernames:
        print("Access granted")
    else:
        print("Access denied")


def basic_operations():
    """practise for basic list operations"""
    numbers = []
    total = 0
    for x in range(5):
        prompt = input("Number: ")
        numbers.append(prompt)
        total += int(prompt)
    average = total / len(numbers)
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(average))


main()
