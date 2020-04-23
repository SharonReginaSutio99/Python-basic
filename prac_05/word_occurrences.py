"""
CP1404/CP5632 Practical
Count the occurences of words in a string
Name: Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""


def print_words(words_to_counts):
    """Format output"""
    max_word_length = max([len(word) for word in words_to_counts.keys()])
    for word, count in words_to_counts.items():
        print("{:{col_width}}:  {}".format(word, count, col_width=max_word_length))


def main():
    text = (input("Text: ")).split()
    text.sort()
    words_to_counts = {}
    for word in text:
        if word in words_to_counts:
            words_to_counts[word] += 1
        else:
            words_to_counts[word] = 1
    print_words(words_to_counts)


main()
