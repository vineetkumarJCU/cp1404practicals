"""
CP1404 Practical 09
Band class
Estimate: 25 minutes
Actual: 21 minutes
"""

class Band:
    """Band class."""

    def __init__(self, name=""):
        """Construct a Band with a name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string to show all musicians in the band play their instruments."""
        for musician in self.musicians:
            print(musician.play())
