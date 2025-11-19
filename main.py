from oops.accessModifiers.Demo import Demo
from oops.accessModifiers.Student import Student
from oops.constructors.BankAccount import BankAccount
from oops.inheritance.Car import Car
from oops.inheritance.ICECar import ICECar
from oops.inheritance.TurboCar import TurboCar
from oops.polymorphism.Calculator import Calculator


def main():
    print("Hello world!")

    tejaSavings = BankAccount("12345", 1234, "Teja", "123", 1000)
    tejaSavings.print_details()

    result = tejaSavings.is_below_min_balance()
    print("Is Below Minimum: " + str(result))

    vikasSavings = BankAccount("12346", 1234, "Vikas", "124", 1000)

    print("Is Below Minimum: " + str(vikasSavings.is_below_min_balance()))

    raviSavings = BankAccount("A1234", 1234, "Ravi", "125", 1000)
    raviSavings.print_details()

    raviSavings2 = BankAccount(raviSavings)
    raviSavings2.print_details()

    st = Student(1, "Sandeep", 100, 22)
    st1 = Student(st)
    st2 = st1
    st.show_marks()
    # Relation between st and st1 -> DEEP
    # Relation between st1 and st2 -> SHALLOW
    # Relation between st and st2 -> INVALID QUES or DEEP

    demo = Demo()
    demo.show_marks(st)

    iceCar = ICECar()
    # new remote new tv
    iceCar.unlock_car()
    iceCar.refuel_car()
    iceCar.change_engine_oil()

    c = ICECar()
    # old remote new tv # implicit casting
    c.change_engine_oil()
    c.unlock_car()
    # c.refuelCar(); -- does not work, as the method is not available in parent
    # -- pressing button in remote that does not exist

    # ICECar ic = (ICECar) new Car(); // explicit casting // down casting // not applicable

    cObj: Car = ICECar()
    # cObj ref variable contains address to ICECar obj
    icObj = cObj
    # icObj [ ref variable of type ICECar ] -> address of ICECar obj
    # using new remote on new TV

    calc = Calculator()

    calc.add(4, 5)
    calc.add(4, 45.5)
    calc.add(5.5, 4)
    calc.add(4.4, 5.5)

    tc = TurboCar()
    tc.start_engine()


main()
