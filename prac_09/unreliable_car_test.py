from prac_09.unreliable_car import UnreliableCar


def main():
    unreliable_car = UnreliableCar("Old Bomb", 100, 50)
    print(f"Created car: {unreliable_car}")

    for i in range(10):
        distance = unreliable_car.drive(10)
        print(f"Attempt {i + 1}: Drove {distance} km. {unreliable_car}")


main()
