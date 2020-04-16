"""
Name: Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""
import random
quick_picks = int(input("How many quick picks? "))
MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_LINE = 6
picks = []
for number_of_picks in range(quick_picks):
    for number in range(NUMBERS_PER_LINE):
        random_number = random.randint(MINIMUM, MAXIMUM)
        while random_number in picks:
            random_number = random.randint(1, 45)
        else:
            picks.append(random_number)
    print(picks)
    picks = []
