from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class TradingStrategyType(Enum):
    MOVING_AVERAGES = 1
    MOMENTUM = 2
    VOLATILITY = 3


@dataclass
class Stock:
    symbol: str
    price: float
    previous_close: float


class TradingIndicatorStrategy(ABC):
    @abstractmethod
    def calculate_indicator(self, stock: Stock) -> float:
        pass


class MovingAverageStrategy(TradingIndicatorStrategy):
    def calculate_indicator(self, stock: Stock) -> float:
        return (stock.price + stock.previous_close) / 2


class MomentumStrategy(TradingIndicatorStrategy):
    def calculate_indicator(self, stock: Stock) -> float:
        return stock.price - stock.previous_close


class VolatilityStrategy(TradingIndicatorStrategy):
    def calculate_indicator(self, stock: Stock) -> float:
        return abs(stock.price - stock.previous_close)


class StockTradingManager:
    def __init__(self, strategy: TradingIndicatorStrategy):
        self.strategy = strategy

    def calculate_indicator(self, stock: Stock) -> float:
        return self.strategy.calculate_indicator(stock)
