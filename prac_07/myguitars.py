"""
CP1404/CP5632 Practical
More Guitars
Estimate: 30 minutes
Actual:
"""

from guitar import Guitar


def main():
    """Set up main"""
    pass

def load_guitars(filename):
    """Load guitars from CSV into a list of Guitar objects."""
    guitars = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


main()