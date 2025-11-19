from oops.accessModifiers.Student import Student


class Demo:
    def show_marks(self, st: Student):  # st.marks = 100
        print(st.marks)  # 100
        self.double_marks(st)
        print(st.marks)  # 200

    def double_marks(self, st: Student):
        st.marks = 2 * st.marks
        print(st.marks)  # 200
        st = None
