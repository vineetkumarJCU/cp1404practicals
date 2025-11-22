from prac_09.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car based on reliability."""
        random_number = randint(0, 100)
        if random_number < self.reliability:
            return super().drive(distance)
        else:
            return 0
