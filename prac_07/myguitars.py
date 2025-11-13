"""
CP1404/CP5632 Practical
More Guitars
Estimate: 30 minutes
Actual: 78 minutes
"""

from guitar import Guitar


def main():
    """Load guitars and display them."""
    guitars = load_guitars("guitars.csv")

    print("These are my guitars:")
    for guitar in guitars:
        print(guitar)

    # Sort by year
    guitars.sort()
    print("\nSorted guitars (oldest to newest):")
    for guitar in guitars:
        print(guitar)

    # Add new guitars from user
    add_new_guitars(guitars)

    # Save guitars to file
    save_guitars("guitars.csv", guitars)


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


def add_new_guitars(guitars):
    """Ask user to add new guitars."""
    print("\nAdd your new guitars:")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")
        name = input("Name: ")


def save_guitars(filename, guitars):
    """Save guitars to a CSV file."""
    with open(filename, "w", encoding="utf-8-sig") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()