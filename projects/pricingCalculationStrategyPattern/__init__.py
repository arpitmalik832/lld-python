from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class PricingType(Enum):
    DISTANCE_BASED = 1
    TIME_BASED = 2
    SURGE = 3


@dataclass
class RideDetails:
    distance: float
    duration: float


class PricingManager:
    def __init__(self, pricing_strategy: "PricingStrategy") -> None:
        self.pricing_strategy = pricing_strategy

    def calculate_price(self, ride_details: RideDetails) -> float:
        return self.pricing_strategy.calculate_price(ride_details)


class PricingStrategy(ABC):
    BASE_FARE = 5.0  # Base fare amount
    PER_KILOMETER_RATE = 2.0  # Rate per kilometer
    PER_MINUTE_RATE = 0.5  # Rate per minute
    SURGE_MULTIPLIER = 2.0  # Surge pricing multiplier

    @abstractmethod
    def calculate_price(self, ride_details: RideDetails) -> float:
        pass


class DistanceBasedPricingStrategy(PricingStrategy):
    def calculate_price(self, ride_details: RideDetails) -> float:
        return self.BASE_FARE + self.PER_KILOMETER_RATE * ride_details.distance


class TimeBasedPricingStrategy(PricingStrategy):
    def calculate_price(self, ride_details: RideDetails) -> float:
        return self.BASE_FARE + self.PER_MINUTE_RATE * ride_details.duration


class SurgePricingStrategy(PricingStrategy):
    def calculate_price(self, ride_details: RideDetails) -> float:
        return self.BASE_FARE * self.SURGE_MULTIPLIER
