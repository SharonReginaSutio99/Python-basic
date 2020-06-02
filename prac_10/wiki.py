"""
CP1404/CP5632 Practical
Try out Wikipedia API
Name: Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""

import wikipedia


def test_wiki():
    loop = True
    while loop:
        search_phrase = input("Insert page title or search phrase to see summary:")
        if search_phrase != "":
            page = wikipedia.page(search_phrase)
            print(page.title)
            print(page.url)
            wikipedia.search(search_phrase)
            try:
                print(wikipedia.summary(search_phrase))
            except wikipedia.exceptions.DisambiguationError as e:
                print(e.options)
        else:
            loop = False


test_wiki()
