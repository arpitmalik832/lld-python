from oops.interfacesAndAbstractClasses.Airbus import Airbus
from oops.interfacesAndAbstractClasses.Boeing import Boeing


def main():
    a = Airbus()
    a.fly()
    a.land()

    b = Boeing()
    b.carry_luggage()
    b.land()


main()
