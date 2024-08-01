from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    menu = "q)uit, c)hoose taxi, d)rive"
    current_taxi = None
    total_cost = 0
    taxis = [Taxi("Prius", 100, 1.23), SilverServiceTaxi("Limo", 100, 1.23, 2), SilverServiceTaxi("Hummer", 200, 1.23, 4)]
    print("Let's drive!")
    print(menu)
    choice = input(">>>").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi:
                cost = drive_taxi(current_taxi)
                total_cost += cost
                print(f"Your Prius trip cost you ${cost:.2f}")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_cost:.2f}")
        print(menu)
        choice = input(">>> ").lower()

    print(f"Total trip cost:{total_cost:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def drive_taxi(taxi):
    distance = float(input("Drive how far? "))
    taxi.start_fare()
    taxi.drive(distance)
    return taxi.get_fare()


def choose_taxi(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

    taxi_choice = int(input("Choose taxi: "))
    while taxi_choice < 0 or taxi_choice >= len(taxis):
        print("Invalid taxi choice.")
        taxi_choice = int(input("Choose taxi: "))
    return taxis[taxi_choice]

main()