from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


class ConnectionPool(ABC):

    @staticmethod
    def get_instance(n: int) -> ConnectionPool:
        pass

    @staticmethod
    def reset_instance() -> None:
        pass

    @abstractmethod
    def initialize_pool(self) -> None:
        pass

    @abstractmethod
    def get_connection(self) -> Optional[DatabaseConnection]:
        pass

    @abstractmethod
    def release_connection(self, connection: DatabaseConnection) -> None:
        pass

    @abstractmethod
    def get_available_connections_count(self) -> int:
        pass

    @abstractmethod
    def get_total_connections_count(self) -> int:
        pass


class ConnectionPoolImpl(ConnectionPool):
    __instance = None

    def __init__(self, n: int):
        self.available_connections = []
        self.used_connections = []
        self.max_connections = n
        self.initialize_pool()

    @staticmethod
    def get_instance(n: int) -> ConnectionPool:
        if ConnectionPoolImpl.__instance is None:
            ConnectionPoolImpl.__instance = ConnectionPoolImpl(n)
        return ConnectionPoolImpl.__instance

    @staticmethod
    def reset_instance() -> None:
        ConnectionPoolImpl.__instance = None

    def initialize_pool(self) -> None:
        self.available_connections = [
            DatabaseConnection() for _ in range(self.max_connections)
        ]
        self.used_connections = []

    def get_connection(self) -> Optional[DatabaseConnection]:
        if self.available_connections is None:
            return None

        connection = self.available_connections.pop()
        self.used_connections.append(connection)
        return connection

    def release_connection(self, connection: DatabaseConnection) -> None:
        if connection is None:
            return

        if connection in self.used_connections:
            self.used_connections.remove(connection)
            self.available_connections.append(connection)

    def get_available_connections_count(self) -> int:
        return len(self.available_connections)

    def get_total_connections_count(self) -> int:
        return len(self.available_connections) + len(self.used_connections)


@dataclass
class DatabaseConnection:
    pass
