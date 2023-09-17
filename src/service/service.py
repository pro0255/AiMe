import os
from src.chat.boilerplate_ai import AI
from src.db.messages import MessagesModel
from src.db.user import UserModel
from pydantic import BaseModel
from src.db.db import DBMessage, MessageType


class AskMessage(BaseModel):
    content: str


class HistoryMessage(AskMessage):
    type: MessageType


class ResponseMessage(BaseModel):
    content: str


class DebugMessage(BaseModel):
    content: str
    type: MessageType


class ResponseDebugMessage(BaseModel):
    messages: list[DebugMessage]


def create_ask_response(
    ai_response: str, user_token: str
) -> ResponseMessage or ResponseDebugMessage:
    env_value = os.getenv("CHAT_ENTITY")

    if env_value == "openai":
        return ResponseMessage(content=ai_response)
    elif env_value == "mock":
        return ResponseMessage(content=ai_response)
    else:
        conversation = MessagesModel.get(user_token)
        response_messages = [
            DebugMessage(content=message.content, type=message.type)
            for message in conversation
        ]
        return ResponseDebugMessage(messages=response_messages)


class Service:
    def __init__(self, ai: AI) -> None:
        self.ai = ai

    def respond(
        self, message_content: str, user_token: str
    ) -> ResponseMessage or ResponseDebugMessage:
        user = UserModel.get(user_token)
        conversation = MessagesModel.get(user)

        ai_response = self.ai.respond(message_content, conversation)

        MessagesModel.upsert(
            user,
            [
                DBMessage(type=MessageType.client, content=message_content),
                DBMessage(type=MessageType.ai, content=ai_response),
            ],
        )

        return create_ask_response(ai_response, user_token)

    def set_conversation(self, history: list[HistoryMessage], user_token: str) -> None:
        user = UserModel.get(user_token)
        MessagesModel.reset(user)
        MessagesModel.upsert(user, history)

    def reset_conversation(self, user_token: str) -> None:
        user = UserModel.get(user_token)
        MessagesModel.reset(user)
