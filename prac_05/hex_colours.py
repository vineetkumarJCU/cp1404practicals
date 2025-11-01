"""
CP1404/CP5632 Practical
Hex Colours Program
"""

COLOUR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "Amaranth": "#e52b50",
    "Amber": "#ffbf00",
    "Amethyst": "#9966cc",
    "AntiqueWhite": "#faebd7",
    "Apricot": "#fbceb1",
    "Beaver": "#9f8170",
    "Black": "#000000",
    "Beige": "#f5f5dc",
    "Burgundy": "#800020"
}


def main():
    """Hexadecimal colour codes by name."""
    colour_name = input("Enter colour name: ").title()
    while colour_name != "":
        try:
            print(f"{colour_name} is {COLOUR_TO_HEX[colour_name]}")
        except KeyError:
            print("Invalid colour name")
        colour_name = input("Enter colour name: ").title()


main()