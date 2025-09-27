"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

def main():
    score = float(input("Enter score: "))
    category = (get_result(score))
    print(f"A score of {score} is {category}")

    # Generate random score
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score})

def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()