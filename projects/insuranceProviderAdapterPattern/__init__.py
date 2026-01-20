from abc import ABC, abstractmethod
from enum import Enum


class AutoProtectStatus:
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    DENIED = "DENIED"


class ClaimStatus(Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"


class AutoProtectApi:
    def add_claim(self, amount):
        print("Submitting claim to AutoProtect")

    def get_status(self, claim_id):
        print("Getting claim status from AutoProtect")
        return AutoProtectStatus.APPROVED


class TravelGuardApi:
    def submit_claim(self, claim_id, amount):
        print("Submitting claim to TravelGuard")

    def get_claim_status(self, claim_id):
        print("Getting claim status from TravelGuard")
        return "SUCCESS"


class TravelInsuranceAdapter(ABC):
    @abstractmethod
    def add_claim(self, claim_id, amount):
        pass

    @abstractmethod
    def get_status(self, claim_id) -> ClaimStatus:
        pass


class TravelGuardAdapter(TravelInsuranceAdapter):
    def __init__(self):
        self.api = TravelGuardApi()

    def add_claim(self, claim_id, amount):
        self.api.submit_claim(claim_id, amount)

    def get_status(self, claim_id) -> ClaimStatus:
        status = self.api.get_claim_status(claim_id)

        if status == "SUCCESS":
            return ClaimStatus.APPROVED
        return ClaimStatus.PENDING


class AutoProtectAdapter(TravelInsuranceAdapter):
    def __init__(self):
        self.api = AutoProtectApi()

    def add_claim(self, claim_id, amount):
        self.api.add_claim(amount)

    def get_status(self, claim_id) -> ClaimStatus:
        status = self.api.get_status(claim_id)

        if status == AutoProtectStatus.APPROVED:
            return ClaimStatus.APPROVED
        return ClaimStatus.PENDING
