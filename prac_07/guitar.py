"""
CP1404/CP5632 Practical 07
Guitar class
"""

from datetime import date


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Compare guitars by year for sorting."""
        return self.year < other.year

    def get_age(self):
        """Return the guitar's age in years."""
        current_year = date.today().year
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old."""
        return self.get_age() >= 50

