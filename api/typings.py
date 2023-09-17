from pydantic import BaseModel
from db.db import MessageType

class AskMessage(BaseModel):
    content: str

class HistoryMessage(AskMessage):
    type: MessageType
    
    

