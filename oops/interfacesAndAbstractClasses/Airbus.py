from oops.interfacesAndAbstractClasses.Aeroplane import Aeroplane


class Airbus(Aeroplane):

    def fly(self):
        print("Airbus is flying")

    def land(self):
        print("Airbus is landing")

    def taxi(self):
        print("Airbus is moving on the ground")
