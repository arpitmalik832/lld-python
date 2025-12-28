from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")


class Prototype(ABC, Generic[T]):
    @abstractmethod
    def copy(self) -> T:
        pass


class Student(Prototype["Student"]):
    def __init__(self, *args):
        if len(args) == 10:
            self.id = args[0]
            self.name = args[1]
            self.psp = args[2]
            self.contactDetails = args[3]
            self.batchId = args[4]
            self.instructorId = args[5]
            self.moduleName = args[6]
            self.batchPsp = args[7]
            self.batchAttendance = args[8]
            self.batchTiming = args[9]
        elif len(args) == 1:
            self.__init__(
                args[0].id,
                args[0].name,
                args[0].psp,
                args[0].contactDetails,
                args[0].batchId,
                args[0].instructorId,
                args[0].moduleName,
                args[0].batchPsp,
                args[0].batchAttendance,
                args[0].batchTiming,
            )

    # getters and setters
    def get_id(self) -> str:
        return self.id

    def set_id(self, id: str):
        self.id = id

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_psp(self) -> float:
        return self.psp

    def set_psp(self, psp: float):
        self.psp = psp

    def get_contact_details(self) -> str:
        return self.contactDetails

    def set_contact_details(self, contact_details: str):
        self.contactDetails = contact_details

    def get_batch_id(self) -> int:
        return self.batchId

    def set_batch_id(self, batch_id: int):
        self.batchId = batch_id

    def get_instructor_id(self) -> int:
        return self.instructorId

    def set_instructor_id(self, instructor_id: int):
        self.instructorId = instructor_id

    def get_module_name(self) -> str:
        return self.moduleName

    def set_module_name(self, module_name: str):
        self.moduleName = module_name

    def get_batch_psp(self) -> float:
        return self.batchPsp

    def set_batch_psp(self, batch_psp: float):
        self.batchPsp = batch_psp

    def get_batch_attendance(self) -> float:
        return self.batchAttendance

    def set_batch_attendance(self, batch_attendance: float):
        self.batchAttendance = batch_attendance

    def get_batch_timing(self) -> str:
        return self.batchTiming

    def set_batch_timing(self, batch_timing: str):
        self.batchTiming = batch_timing

    def copy(self) -> "Student":
        copy = Student()
        copy.batchId = self.batchId
        copy.instructorId = self.instructorId
        copy.moduleName = self.moduleName
        copy.batchPsp = self.batchPsp
        copy.batchAttendance = self.batchAttendance
        copy.batchTiming = self.batchTiming
        return copy

    class Builder:
        def __init__(self):
            self.id = None
            self.name = None
            self.psp = None
            self.contactDetails = None
            self.batchId = None
            self.instructorId = None
            self.moduleName = None
            self.batchPsp = None
            self.batchAttendance = None
            self.batchTiming = None

        def id(self, id: int) -> "Student.Builder":
            self.id = id
            return self

        def name(self, name: str) -> "Student.Builder":
            self.name = name
            return self

        def psp(self, psp: float) -> "Student.Builder":
            self.psp = psp
            return self

        def contact_details(self, contact_details: str) -> "Student.Builder":
            self.contactDetails = contact_details
            return self

        def batch_id(self, batch_id: int) -> "Student.Builder":
            self.batchId = batch_id
            return self

        def instructor_id(self, instructor_id: int) -> "Student.Builder":
            self.instructorId = instructor_id
            return self

        def module_name(self, module_name: str) -> "Student.Builder":
            self.moduleName = module_name
            return self

        def batch_psp(self, batch_psp: float) -> "Student.Builder":
            self.batchPsp = batch_psp
            return self

        def batch_attendance(self, batch_attendance: float) -> "Student.Builder":
            self.batchAttendance = batch_attendance
            return self

        def batch_timing(self, batch_timing: str) -> "Student.Builder":
            self.batchTiming = batch_timing
            return self

        def validate(self):
            pass

        def build(self) -> "Student":
            self.validate()
            return Student(self)


def main():
    pass


main()
