"""
CP1404/CP5632 Practical
Wimbledon File
Estimate: 35 minutes
Actual: 73 minutes
"""

def main():
    """Display Wimbledon champions and their countries from CSV file."""
    records = read_data("wimbledon.csv")
    champion_wins = count_champions(records)
    display_champions(champion_wins)
    print()
    display_countries(records)


def read_data(filename):
    """Read data from CSV file and return list of records."""
    with open(filename, "r", encoding="utf-8-sig") as file:
        file.readline()
        return [line.strip().split(",") for line in file]


def count_champions(records):
    champions = {}
    for record in records:
        name = record[2]
        if name in champions:
            champions[name] += 1
        else:
            champions[name] = 1
    return champions


def display_champions(champion_wins):
    """Print champions and how many times each has won."""
    print("Wimbledon Champions:")
    for name, wins in champion_wins.items():
        print(f"{name:20} {wins}")


def display_countries(records):
    """Print all countries of winners."""
    countries = sorted({record[1] for record in records})
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


main()