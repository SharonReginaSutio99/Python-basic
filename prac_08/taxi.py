"""
CP1404/CP5632 Practical
Taxi class
Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""
from prac_08.car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""

    price_per_km = 1.23  # Class variable shared across Taxi objects

    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(),
                                                             self.current_fare_distance,
                                                             self.price_per_km)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return round(self.price_per_km * self.current_fare_distance,1)

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
