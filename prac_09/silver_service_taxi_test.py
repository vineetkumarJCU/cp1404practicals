from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    hummer = SilverServiceTaxi("Hummer", 200, 2)
    hummer.drive(18)
    print(hummer)
    fare = hummer.get_fare()
    print(f"Fare: ${fare:.2f}")

    assert abs(fare - 48.78) < 0.01, f"Test failed! Expected $48.78 but got ${fare:.2f}"

    print("All tests passed!")


main()
