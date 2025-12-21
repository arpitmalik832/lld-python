from designPatterns.creationalDesignPatterns.builder.way1.Student import Student
from designPatterns.creationalDesignPatterns.builder.way1.StudentHelper import (
    StudentHelper,
)


def main():
    helper = StudentHelper()
    helper.set_id("1234").set_name("ABC").set_marks(90).set_roll("1234").set_mobile(
        "1234567890"
    ).set_email("abc@email.com").set_intermediate_year(2022).set_intermediate_roll(
        "FE13"
    ).set_intermediate_school(
        "APS"
    ).set_intermediate_marks(
        60
    )

    s = Student.build(helper)

    print(s)


main()
