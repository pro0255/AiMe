
from pydantic import BaseModel
from enum import Enum


class MessageType(str, Enum):
    ai = "ai"
    client = "client"


class DBMessage(BaseModel):
  type: MessageType
  content: str


class MemoryDatabase():
  def __init__(self):
    self.db: dict[str, list[DBMessage]] = {}
    

db_instance = MemoryDatabase()

