from abc import ABC, abstractmethod

from typing import TypeVar, Generic

T = TypeVar("T")


class Prototype(ABC, Generic[T]):
    @abstractmethod
    def copy(self) -> T:
        pass


class Student(Prototype["Student"]):
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__psp = None
        self.__contactDetails = None
        self.__batchId = None
        self.__instructorId = None
        self.__moduleName = None
        self.__batchPsp = None
        self.__batchAttendance = None
        self.__batchTiming = None

    # getters and setters
    def get_id(self) -> str:
        return self.__id

    def set_id(self, id: str):
        self.__id = id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_psp(self) -> float:
        return self.__psp

    def set_psp(self, psp: float):
        self.__psp = psp

    def get_contact_details(self) -> str:
        return self.__contactDetails

    def set_contact_details(self, contact_details: str):
        self.__contactDetails = contact_details

    def get_batch_id(self) -> int:
        return self.__batchId

    def set_batch_id(self, batch_id: int):
        self.__batchId = batch_id

    def get_instructor_id(self) -> int:
        return self.__instructorId

    def set_instructor_id(self, instructor_id: int):
        self.__instructorId = instructor_id

    def get_module_name(self) -> str:
        return self.__moduleName

    def set_module_name(self, module_name: str):
        self.__moduleName = module_name

    def get_batch_psp(self) -> float:
        return self.__batchPsp

    def set_batch_psp(self, batch_psp: float):
        self.__batchPsp = batch_psp

    def get_batch_attendance(self) -> float:
        return self.__batchAttendance

    def set_batch_attendance(self, batch_attendance: float):
        self.__batchAttendance = batch_attendance

    def get_batch_timing(self) -> str:
        return self.__batchTiming

    def set_batch_timing(self, batch_timing: str):
        self.__batchTiming = batch_timing

    def copy(self) -> "Student":
        copy = Student()
        copy.__batchId = self.__batchId
        copy.__instructorId = self.__instructorId
        copy.__moduleName = self.__moduleName
        copy.__batchPsp = self.__batchPsp
        copy.__batchAttendance = self.__batchAttendance
        copy.__batchTiming = self.__batchTiming
        return copy


def main():
    lldMWFBatch = Student()
    lldMWFBatch.set_batch_id(1)
    lldMWFBatch.set_instructor_id(1)
    lldMWFBatch.set_batch_attendance(100)
    lldMWFBatch.set_batch_psp(90)
    lldMWFBatch.set_module_name("LLD")
    lldMWFBatch.set_batch_timing("MWF 10:00 AM - 11:00 AM")

    # Student rohit from lld batch
    rohit = lldMWFBatch.copy()
    rohit.set_id("10")
    rohit.set_name("Rohit")
    rohit.set_psp(80)
    rohit.set_contact_details("Place A, City B")
