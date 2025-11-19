class Student:
    # id
    # name
    # marks
    # roll

    def __init__(self, *args):
        # parameterized constructor
        if len(args) == 4:
            self.id = args[0]
            self.name = args[1]
            self.marks = args[2]
            self.roll = args[3]
        # copy constructor
        elif len(args) == 1:
            self.__init__(args[0].id, args[0].name, args[0].marks, args[0].roll)

    def show_marks(self):
        x = 100
        print("X = " + str(x))
        self.double_marks(x)
        print("X = " + str(x))

    def double_marks(self, x):
        x = x * 2
        print(x)
