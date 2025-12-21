from __future__ import annotations

import os
from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum


class LogLevel(Enum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4


class Logger(ABC):

    @staticmethod
    def get_instance() -> Logger:
        pass

    @staticmethod
    def reset_instance() -> None:
        pass

    @abstractmethod
    def log(self, level: LogLevel, message: str) -> None:
        pass

    @abstractmethod
    def set_log_file(self, file_path: str) -> None:
        pass

    @abstractmethod
    def get_log_file(self) -> str:
        pass

    @abstractmethod
    def flush(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass


class LoggerImpl(Logger):
    __instance = None

    def __init__(self):
        self.__file = None
        self.__log_file_path = None

    @staticmethod
    def get_instance() -> Logger:
        if LoggerImpl.__instance is None:
            LoggerImpl.__instance = LoggerImpl()
        return LoggerImpl.__instance

    @staticmethod
    def reset_instance() -> None:
        LoggerImpl.__instance = None

    def log(self, level: LogLevel, message: str) -> None:
        if self.__file is None:
            raise RuntimeError("Logger not initialized. Call set_log_file() first.")

        if level is None:
            raise ValueError("Level must not be None.")

        if message is None:
            message = "null"

        timestamp = datetime.now().astimezone().isoformat()
        log_entry = f"{timestamp} [{level.value}] {message}\n"

        try:
            self.__file.write(log_entry)
            self.__file.flush()
        except Exception as e:
            raise RuntimeError(
                f"Failed to write log entry to file: {self.__log_file_path}"
            ) from e

    def set_log_file(self, file_path: str) -> None:
        if not file_path or file_path.strip() == "":
            raise ValueError("file_path must not be null or blank.")

            # Close an existing file if reinitializing
        if self.__file is not None:
            self.__file.close()

        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            self.__file = open(file_path, "a", encoding="utf-8")
            self.__log_file_path = file_path
        except OSError as e:
            raise RuntimeError(f"Unable to open log file: {file_path}") from e

    def get_log_file(self) -> str:
        return self.__log_file_path

    def flush(self) -> None:
        if self.__file:
            self.__file.flush()

    def close(self) -> None:
        if self.__file is None:
            raise RuntimeError("Logger not initialized. Call set_log_file() first.")
        self.__file.close()
        self.__file = None
