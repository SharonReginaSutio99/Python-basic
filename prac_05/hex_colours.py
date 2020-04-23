"""
CP1404/CP5632 Practical
Hexadecimal color codes in dictionary
Name: Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""

COLOR_TO_CODE = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1": "#7fffd4",
                 "azure1": "#f0ffff", "beige": "#f5f5dc", "bisque1": "#ffe4c4",
                 "BlanchedAlmond": "#ffebcd", "blue1": "#0000ff", "BlueViolet": "#8a2be2",
                 "Black": "000000"}


def print_colors():
    max_key_length = max([len(key) for key in COLOR_TO_CODE.keys()])
    for color, code in COLOR_TO_CODE.items():
        print("{:{col_width}} - {}".format(color, code, col_width=max_key_length))


def main():
    print_colors()
    color_to_code = {color.lower(): code for color, code in COLOR_TO_CODE.items()}
    color_name = input("Enter color name: ").strip().lower()
    while color_name != "":
        print("Color code is {} for {}".format(color_to_code.get(color_name), color_name))
        color_name = input("Enter color name: ").strip().lower()

main()
