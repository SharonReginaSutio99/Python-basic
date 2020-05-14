"""
CP1404/CP5632 Practical
Taxi Simulator
Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""
from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """A taxi simulator program which allow user to be presented with a list of available taxis and choose one, say how
    far they want to drive and at the end of each trip the price and bill will be shown and added. This repeats until
    user quits."""

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0

    print("Let's drive!")
    user_choice = input("q(uit), c)hoose taxi, d)rive\n>>>").upper()

    while user_choice != "Q":
        if user_choice == "C":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]

        elif user_choice == "D":
            current_taxi.start_fare()
            driving_distance = int(input("Drive how far?"))
            current_taxi.drive(driving_distance)
            trip_cost = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
            total_bill += trip_cost

        else:
            print("Invalid Option")
        print("Bill to date: ${:.2f}".format(total_bill))
        user_choice = input("q(uit), c)hoose taxi, d)rive\n>>>").upper()
    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display taxis and their details."""
    for index, taxi in enumerate(taxis):
        print("{} - {}".format(index, taxi))


def run_tests():
    """Test the Car and Taxi class to show they're working."""
    # Test Car Class
    ferrari = Car("Ferrari", 1000)
    ferrari.drive(333)
    print("Ferrari fuel:{}".format(ferrari.fuel))
    print("Ferrari odometer:{}".format(ferrari.odometer))
    ferrari.drive(200)
    print("Ferrari fuel after driving another 200km:{}".format(ferrari.fuel))
    print("Ferrari odo after driving another 200km:{}".format(ferrari.odometer))
    print(ferrari)

    # Test Taxi Class
    truck = Taxi("Hyundai", 500)
    truck.start_fare()
    truck.drive(333)
    print("Current fare distance of truck is{}".format(truck.current_fare_distance))
    print("Fare of Taxi Hyundai after driving 333 is {}".format(truck.get_fare()))

    # Test SilverServiceClass
    truck = SilverServiceTaxi("Hyundai", 500, 1)
    truck.start_fare()
    truck.drive(333)
    print("Fare of SilverServiceTaxi Hyundai after driving 333 is {}".format(truck.get_fare()))


main()
