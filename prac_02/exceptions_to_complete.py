"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input("Please enter a valid integer."))
        finished = True
    except ValueError:
        print("Invalid (not an integer)")
print("Valid result is:", result)
