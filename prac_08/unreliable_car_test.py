from prac_08.unreliable_car import UnreliableCar


def main():
    """Test UnreliableCars."""
    good_car = UnreliableCar("Good car", 100, 90)
    bad_car = UnreliableCar("Bad car", 100, 9)

    # test the randomness by driving the car 10 times in a distance range 1-10km
    # print the distance driven
    for i in range(1, 11):
        print("Drive attempt {}".format(i))
        print("Distance driven by {} is {} km.".format(good_car.name, good_car.drive(i)))
        print("Distance driven by {} is {} km.".format(bad_car.name, bad_car.drive(i)))

    # print final status of the cars
    print(good_car)
    print(bad_car)


main()
