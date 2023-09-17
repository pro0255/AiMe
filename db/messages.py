from db.db import DBMessage, db_instance


class MessagesModel():
  @staticmethod
  def get(user_token: str) -> list[DBMessage]:
    return db_instance.db.get(user_token, [])
  
  @staticmethod
  def upsert(user_token: str, messages: list[DBMessage]) -> None:
    db_instance.db[user_token] = db_instance.db.get(user_token, []) + messages 
  
  @staticmethod
  def reset(user_token: str) -> None:
    db_instance.db[user_token] = []
  
  
  
  
  
  