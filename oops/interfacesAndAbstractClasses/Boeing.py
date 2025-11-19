from oops.interfacesAndAbstractClasses.Aeroplane import Aeroplane
from oops.interfacesAndAbstractClasses.LuggageCarrier import LuggageCarrier


class Boeing(Aeroplane, LuggageCarrier):
    def fly(self):
        print("Boeing plane is flying")

    def land(self):
        print("Boeing plane is landing")

    def taxi(self):
        print("Boeing plane is moving on ground")

    def carry_luggage(self):
        print("Boeing plane is carrying luggage")
