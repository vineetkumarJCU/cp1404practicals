"""
Test program for the UnreliableCar class
"""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar over multiple drive attempts."""
    unreliable_car = UnreliableCar("Safari SUV", 100, 50)
    total_distance = 0

    for i in range(10):
        distance = unreliable_car.drive(10)
        total_distance += distance
        print(f"Attempt {i + 1}: Drove {distance} km, total = {total_distance} km")

    print(f"\nFinal Car status: {unreliable_car}")


main()
