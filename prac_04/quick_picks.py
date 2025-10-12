"""
Quick Picks Exercise
"""

import random

MINIMUM_VALUE = 1
MAXIMUM_VALUE = 45
NUMBERS_PER_LINE = 6

def main():
    """Select number of quick picks"""
    number_of_quick_picks = int(input("How many quick picks? >"))
    while number_of_quick_picks < 0:
        print("This is too less! Enter Again.")
        number_of_quick_picks = int(input("How many quick picks? >"))

#  generate each quick pick
    while number_of_quick_picks > 0:
        quick_pick = []
        while len(quick_pick) < NUMBERS_PER_LINE:
            number = random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
            if number not in quick_pick:
                quick_pick.append(number)

        quick_pick.sort()
        print(' '.join(f"{num:2}" for num in quick_pick))
        number_of_quick_picks -= 1  # decrease remaining count

main()