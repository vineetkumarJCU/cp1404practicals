"""
CP1404/CP5632 Practical
State names in a dictionary
"""

CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

def main():
    """Display state names based on user input."""
    print(CODE_TO_NAME)

    state_code = input("Enter short state: ").strip().upper()
    while state_code != "":
        try:
            print(state_code, "is", CODE_TO_NAME[state_code])
        except KeyError:
            print("Invalid short state")
        state_code = input("Enter short state: ").strip().upper()

for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")

main()