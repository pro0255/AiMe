from chat.boilerplate_ai import AI
from db.db import DBMessage


class DebugAI(AI):
    def respond(self, message_content: str, history: list[DBMessage] = []) -> str:
        return f"""Message content={message_content}\nHistory={len(history)}"""
