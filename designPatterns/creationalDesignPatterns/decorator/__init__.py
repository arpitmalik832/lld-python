from abc import ABC, abstractmethod


class IceCream(ABC):
    @abstractmethod
    def get_cost(self) -> int:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass


class ChocolateChip(IceCream):
    def __init__(self, ice_cream: IceCream):
        if ice_cream is None:
            raise Exception("Ice Cream cannot be null")
        self.__iceCream = ice_cream

    def get_cost(self) -> int:
        return self.__iceCream.get_cost() + 10

    def get_description(self) -> str:
        return self.__iceCream.get_description() + ", Chocolate Chip"


class ChocolateCone(IceCream):
    def __init__(self, *args):
        if len(args) == 0:
            self.__iceCream = None
        else:
            self.__iceCream = args[0]

    def get_cost(self) -> int:
        if self.__iceCream is not None:
            return self.__iceCream.get_cost() + 30
        return 30

    def get_description(self) -> str:
        if self.__iceCream is not None:
            return self.__iceCream.get_description() + ", Chocolate Cone"
        return "Chocolate Cone"


class ChocolateScoop(IceCream):
    def __init__(self, ice_cream: IceCream):
        if ice_cream is None:
            raise Exception("Ice Cream cannot be null")
        self.__iceCream = ice_cream

    def get_cost(self) -> int:
        return self.__iceCream.get_cost() + 30

    def get_description(self) -> str:
        return self.__iceCream.get_description() + ", Chocolate Scoop"


class VanillaCone(IceCream):
    def __init__(self, *args):
        if len(args) == 0:
            self.__iceCream = None
        else:
            self.__iceCream = args[0]

    def get_cost(self) -> int:
        if self.__iceCream is not None:
            return self.__iceCream.get_cost() + 20
        return 20

    def get_description(self) -> str:
        if self.__iceCream is not None:
            return self.__iceCream.get_description() + ", Vanilla Cone"
        return "Vanilla Cone"


class VanillaScoop(IceCream):
    def __init__(self, ice_cream: IceCream):
        if ice_cream is None:
            raise Exception("Ice Cream cannot be null")
        self.__iceCream = ice_cream

    def get_cost(self) -> int:
        return self.__iceCream.get_cost() + 25

    def get_description(self) -> str:
        return self.__iceCream.get_description() + ", Vanilla Scoop"


def main():
    i1 = VanillaCone()
    print("Description: " + i1.get_description())
    print(f"Cost: {i1.get_cost()}")

    # vanilla cone with chocolate scoop ice cream
    i2 = ChocolateScoop(VanillaCone())
    print("Description: " + i2.get_description())
    print(f"Cost: {i2.get_cost()}")

    # vanilla cone, chocolate scoop, choco cone, vanilla scoop, choco chip
    i3 = ChocolateChip(VanillaScoop(ChocolateCone(ChocolateScoop(VanillaCone()))))
    print(f"Description: {i3.get_description()}")
    print(f"Cost: {i3.get_cost()}")


main()
