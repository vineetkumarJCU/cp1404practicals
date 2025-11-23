"""
CP1404 Practical 09
Taxi Simulator Practical Exercise
Estimate: 30 minutes
Actual:
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    print("Let's drive!")
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    bill_to_date = 0.0

    menu = "q)uit, c)hoose taxi, d)rive"
    print(menu)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            pass
        elif choice == "d":
            pass
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(menu)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")


