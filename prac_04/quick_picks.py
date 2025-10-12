"""
Quick Picks Exercise
"""

MINIMUM_VALUE = 1
MAXIMUM_VALUE = 45
NUMBERS_PER_LINE = 6

def main():
    """Select number of quick picks"""
    number_of_quick_picks = int(input("How many quick picks? >"))
    while number_of_quick_picks < 0:
        print("This is too less! Enter Again.")
        number_of_quick_picks = int(input("How many quick picks? >"))

main()