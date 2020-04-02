"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# TODO: Fix this!

def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid input")
        score = float(input("Enter score: "))
    else:
        if score >= 90:
            print("Excellent")
        elif 50 <= score < 90:
            print("Passable")
        else:
            print("Bad")


main()
