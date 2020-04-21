"""
CP1404/CP5632 Practical
Hexadecimal color codes in dictionary
Name: Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""

CODE_TO_NAME = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1": "#7fffd4",
                "azure1": "#f0ffff", "beige": "#f5f5dc", "bisque1": "#ffe4c4",
                "BlanchedAlmond": "#ffebcd", "blue1": "#0000ff", "BlueViolet": "#8a2be2",
                "Black": "000000"}
print(CODE_TO_NAME)

color_name = input("Enter color name: ").upper()
while color_name != "":
    if color_name in CODE_TO_NAME.upper():
        print("{} is {}".format(color_name, CODE_TO_NAME[color_name]))
