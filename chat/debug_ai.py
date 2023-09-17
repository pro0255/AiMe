from chat.boilerplate_ai import AI
from db.db import DBMessage


class DebugAI(AI):
    def respond(self, message_content: str, history: list[DBMessage] = []) -> str:
        return f"AI MESSAGE - asked client {message_content}; index {len(history)}"
