from chat.boilerplate_ai import AI
from db.messages import MessagesModel
from db.user import UserModel
from pydantic import BaseModel
from db.db import MessageType

class AskMessage(BaseModel):
    content: str

class HistoryMessage(AskMessage):
    type: MessageType

class Service():
  def __init__(self, ai: AI) -> None:
    self.ai = ai
    
  def respond(self, message_content: str, user_token: str) -> str:
    user = UserModel.get(user_token)
    conversation = MessagesModel.get(user)
    
    ai_response = self.ai.respond(message_content, conversation)
    
    MessagesModel.upsert(user, [ai_response])
    
    return ai_response
  
  
  def set_conversation(self, history: list[HistoryMessage], user_token: str) -> None:
    user = UserModel.get(user_token)
    MessagesModel.reset(user)
    MessagesModel.upsert(user, history)
    
    
  def reset_conversation(self, user_token: str) -> None:
    user = UserModel.get(user_token)
    MessagesModel.reset(user)
    
    
    
    
    
    
    
  
  
  