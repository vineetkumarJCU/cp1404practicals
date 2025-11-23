"""
CP1404 Practical 09
SilverServiceTaxi
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi with a fare multiplier and flagfall cost."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Multiply instance price_per_km by fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the fare including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation including flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

