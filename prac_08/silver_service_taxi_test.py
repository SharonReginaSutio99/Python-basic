"""
CP1404/CP5632 Practical
Test SilverServiceTaxi Class
Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test Silver Service Taxis"""
    hummer_taxi = SilverServiceTaxi("Hummer", 200, 2)
    print(hummer_taxi)
    hummer_taxi.drive(18)
    print("Fare: $ {:.2f}".format(hummer_taxi.get_fare()))


main()
