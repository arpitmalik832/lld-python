from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Generic, TypeVar

T = TypeVar("T")


class Builder(ABC, Generic[T]):

    @abstractmethod
    def build(self) -> T:
        pass


@dataclass
class DatabaseConfiguration:
    database_url: str
    username: str
    password: str
    max_connections: int
    enable_cache: bool
    is_read_only: bool

    @staticmethod
    def builder() -> "DatabaseBuilder":
        return DatabaseConfiguration.DatabaseBuilder()

    def __init__(self, *args):
        if len(args) == 1:
            builder = args[0]
            self.database_url = builder.database_url
            self.username = builder.username
            self.password = builder.password
            self.max_connections = builder.max_connections
            self.enable_cache = builder.enable_cache
            self.is_read_only = builder.is_read_only
        else:
            self.database_url = args[0]
            self.username = args[1]
            self.password = args[2]
            self.max_connections = args[3]
            self.enable_cache = args[4]
            self.is_read_only = args[5]

    class DatabaseBuilder(Builder["DatabaseConfiguration"]):

        def __init__(self):
            self._instance = DatabaseConfiguration(None, None, None, None, None, None)

        def set_database_url(
            self, database_url: str
        ) -> "DatabaseConfiguration.DatabaseBuilder":
            self._instance.database_url = database_url
            return self

        def set_username(
            self, username: str
        ) -> "DatabaseConfiguration.DatabaseBuilder":
            self._instance.username = username
            return self

        def set_password(
            self, password: str
        ) -> "DatabaseConfiguration.DatabaseBuilder":
            self._instance.password = password
            return self

        def set_max_connections(
            self, max_connections: int
        ) -> "DatabaseConfiguration.DatabaseBuilder":
            self._instance.max_connections = max_connections
            return self

        def set_enable_cache(
            self, enable_cache: bool
        ) -> "DatabaseConfiguration.DatabaseBuilder":
            self._instance.enable_cache = enable_cache
            return self

        def set_is_read_only(
            self, is_read_only: bool
        ) -> "DatabaseConfiguration.DatabaseBuilder":
            self._instance.is_read_only = is_read_only
            return self

        def build(self) -> "DatabaseConfiguration":
            self._instance = DatabaseConfiguration(self._instance)
            return self._instance


class MessageType(Enum):
    TEXT = "TEXT"
    IMAGE = "IMAGE"
    AUDIO = "AUDIO"
    VIDEO = "VIDEO"


@dataclass
class Message:
    message_type: MessageType
    content: str
    sender: str
    recipient: str
    is_delivered: bool
    timestamp: int

    @staticmethod
    def builder() -> "MessageBuilder":
        return Message.MessageBuilder()

    def __init__(self, *args):
        if len(args) == 1:
            builder = args[0]
            self.message_type = builder.message_type
            self.content = builder.content
            self.sender = builder.sender
            self.recipient = builder.recipient
            self.is_delivered = builder.is_delivered
            self.timestamp = builder.timestamp
        else:
            self.message_type = args[0]
            self.content = args[1]
            self.sender = args[2]
            self.recipient = args[3]
            self.is_delivered = args[4]
            self.timestamp = args[5]

    class MessageBuilder(Builder["Message"]):

        def __init__(self):
            self._instance = Message(None, None, None, None, None, None)

        def message_type(self, message_type: MessageType) -> "Message.MessageBuilder":
            self._instance.message_type = message_type
            return self

        def content(self, content: str) -> "Message.MessageBuilder":
            self._instance.content = content
            return self

        def sender(self, sender: str) -> "Message.MessageBuilder":
            self._instance.sender = sender
            return self

        def recipient(self, recipient: str) -> "Message.MessageBuilder":
            self._instance.recipient = recipient
            return self

        def is_delivered(self, is_delivered: bool) -> "Message.MessageBuilder":
            self._instance.is_delivered = is_delivered
            return self

        def timestamp(self, timestamp: int) -> "Message.MessageBuilder":
            self._instance.timestamp = timestamp
            return self

        def build(self) -> "Message":
            self._instance = Message(self._instance)
            return self._instance


@dataclass
class Query:
    select: str
    from_: str
    where: str
    join: str
    order_by: str
    group_by: str

    def __init__(self, *args):
        if len(args) == 1:
            builder = args[0]
            self.select = builder.select
            self.from_ = builder.from_
            self.where = builder.where
            self.join = builder.join
            self.order_by = builder.order_by
            self.group_by = builder.group_by
        else:
            self.select = args[0]
            self.from_ = args[1]
            self.where = args[2]
            self.join = args[3]
            self.order_by = args[4]
            self.group_by = args[5]

    @staticmethod
    def builder() -> "QueryBuilder":
        return Query.QueryBuilder()

    class QueryBuilder(Builder["Query"]):
        def __init__(self):
            self._instance = Query(None, None, None, None, None, None)

        def select(self, select: str) -> "Query.QueryBuilder":
            self._instance.select = select
            return self

        def from_(self, from_: str) -> "Query.QueryBuilder":
            self._instance.from_ = from_
            return self

        def where(self, where: str) -> "Query.QueryBuilder":
            self._instance.where = where
            return self

        def join(self, join: str) -> "Query.QueryBuilder":
            self._instance.join = join
            return self

        def order_by(self, order_by: str) -> "Query.QueryBuilder":
            self._instance.order_by = order_by
            return self

        def group_by(self, group_by: str) -> "Query.QueryBuilder":
            self._instance.group_by = group_by
            return self

        def build(self) -> "Query":
            self._instance = Query(self._instance)
            return self._instance


def main():
    db_config = (
        DatabaseConfiguration.builder()
        .set_database_url("localhost")
        .set_username("root")
        .set_password("")
        .set_max_connections(10)
        .set_enable_cache(True)
        .set_is_read_only(False)
        .build()
    )
    print(db_config)

    msg = (
        Message.builder().message_type(MessageType.TEXT).content("Hello World").build()
    )
    print(msg)


main()
