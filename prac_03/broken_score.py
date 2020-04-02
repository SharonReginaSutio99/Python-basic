"""
CP1404/CP5632 - Practical
Broken program to determine score status
Name: Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals

"""


def main():
    import random
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid input")
        score = float(input("Enter score: "))
    scale = score_to_scale(score)
    print(scale)
    random_score = score_to_scale(random.randint(0, 100))
    print(random_score)


def score_to_scale(score):
    if score >= 90:
        return "Excellent"
    elif 50 <= score < 90:
        return "Passable"
    else:
        return "Bad"


main()
