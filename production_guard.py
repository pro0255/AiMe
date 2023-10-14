
import os

def production_guard():
  current_env = os.getenv("ENV")
  
  env_value = os.getenv("CHAT_ENTITY")
  
  if(current_env == 'development' and env_value == 'openai'):
    raise "It's not allowed to use openai in development mode"
  
  
  