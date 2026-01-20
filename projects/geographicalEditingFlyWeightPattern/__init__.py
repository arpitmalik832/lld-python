from dataclasses import dataclass
from enum import Enum


class GraphicType(Enum):
    JPEG = "jpeg"
    PNG = "png"
    SVG = "svg"


@dataclass
class Image:
    pass


@dataclass
class Graphic:
    type: GraphicType
    image: Image
    x: int
    y: int
    width: int
    height: int
    color: str


@dataclass
class GraphicIntrinsicState:
    type: GraphicType


@dataclass
class GraphicExtrinsicState:
    pass


from abc import ABC, abstractmethod
from typing import Dict, Optional


class FlyweightRegistry(ABC):

    @abstractmethod
    def add_flyweight(self, flyweight: GraphicIntrinsicState) -> None:
        pass

    @abstractmethod
    def get_flyweight(self, type_: GraphicType) -> Optional[GraphicIntrinsicState]:
        pass


class FlyweightRegistryImpl(FlyweightRegistry):
    def __init__(self):
        self._flyweights: Dict[GraphicType, GraphicIntrinsicState] = {}

    def add_flyweight(self, flyweight: GraphicIntrinsicState) -> None:
        self._flyweights[flyweight.type] = flyweight

    def get_flyweight(self, type_: GraphicType) -> Optional[GraphicIntrinsicState]:
        return self._flyweights.get(type_)
