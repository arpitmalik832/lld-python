from oops.inheritance.Car import Car


class ICECar(Car):
    # engineSize

    def __init__(self):
        print("Executing the ICECar constructor")

    def refuel_car(self):
        print("Refueling the ICECar")
