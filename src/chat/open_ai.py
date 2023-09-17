from src.chat.boilerplate_ai import AI
from src.db.db import DBMessage


class OpenAI(AI):
    def respond(self, message_content: str, history: list[DBMessage] = []) -> str:
        raise NotImplementedError()
