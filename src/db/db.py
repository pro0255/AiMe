from enum import Enum

from pydantic import BaseModel
from expiring_dict import ExpiringDict


TTL_TIME = 60 * 15


class MessageType(str, Enum):
    ai = "ai"
    client = "client"


class DBMessage(BaseModel):
    type: MessageType
    content: str

    def __str__(self) -> str:
        return f"Type={self.type}, Content=${self.content}"


class MemoryDatabase:
    def __init__(self):
        self.db: dict[str, list[DBMessage]] = ExpiringDict(TTL_TIME)


db_instance = MemoryDatabase()
