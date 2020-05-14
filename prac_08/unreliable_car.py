"""
CP1404/CP5632 Practical
UnreliableCar class
Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""
from prac_08.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of Car which has a reliability attribute."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car if the random number generated is less than car's reliability."""
        # Distance driven is 0 if not reliable
        if random.randint(1, 101) >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
