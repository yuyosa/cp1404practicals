"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "My Car")
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car(100, "Limo")
    limo.add_fuel(20)
    print(f"limo has fuel:{limo.fuel}")

    distance = limo.drive(115)
    print(f"Limo drove {distance} km")
    print(f"Limo now has fuel: {limo.fuel}")

    print(my_car)
    print(limo)

main()