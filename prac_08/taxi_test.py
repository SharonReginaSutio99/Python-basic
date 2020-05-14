"""
CP1404/CP5632 Practical
Test Taxi Class
Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""
from prac_08.taxi import Taxi


def main():
    # Taxi.price_per_km = 3 # demo class variable can be changed
    # class variable can be changed, and constants cannot change
    # when sharing is needed across objects of the same class, use class variables

    # Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km
    prius_taxi = Taxi("Prius 1", 100)

    # Drive the taxi 40km
    prius_taxi.drive(40)

    # Print the taxi's details and the current fare
    print(prius_taxi)
    print("Current fare: $ {:.2f}".format(prius_taxi.get_fare()))

    # Restart the meter (start a new fare) and then drive the car 100km
    prius_taxi.start_fare()
    prius_taxi.drive(100)

    # Print the details and the current fare
    print(prius_taxi)
    print("Current fare: $ {:.2f}".format(prius_taxi.get_fare()))


main()
