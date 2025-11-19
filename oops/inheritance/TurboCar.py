from oops.inheritance.Car import Car

class TurboCar (Car):
    def __init__(self):
        print("Executing the TurboCar constructor")

    def __start_engine(self):
        print("Starting engine in the TurboCar")