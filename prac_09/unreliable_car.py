"""
CP1404/CP5632 Practical
UnreliableCar class that inherits from Car
"""
from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised Car class that includes reliability for driving."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car based on reliability."""
        random_number = randint(0, 100)
        if random_number < self.reliability:
            return super().drive(distance)
        else:
            return 0
