"""
CP1404/CP5632 Practical
SilverServiceTaxi Class
Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of Taxi which has fanciness attribute."""

    # extra charge for each new fare
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness=0):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Taxi plus flagfall."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Calculate the total fare of SilverService Taxi."""
        normal_fare = super().get_fare()
        return normal_fare + self.flagfall


