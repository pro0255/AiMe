import os
import secrets

import uvicorn
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from production_guard import production_guard
from src.chat.factory import create_chat_entity
from src.db.db import MessageType
from src.service.service import ResponseDebugMessage, ResponseMessage, Service

load_dotenv()
production_guard()


def parseOrigins():
    origins = os.getenv("ORIGINS")
    return origins.split(";")


origins = parseOrigins()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


service = Service(create_chat_entity())
TOKEN_SYMBOL = "TOKEN_SYMBOL"


class AskMessage(BaseModel):
    content: str


class HistoryMessage(AskMessage):
    type: MessageType


def create_new_user_token():
    print("Creating a new token")
    return secrets.token_hex(32)


def create_cookie(response: Response, request: Request):
    request_cookie_token = request.cookies.get(TOKEN_SYMBOL)
    if request_cookie_token:
        return request_cookie_token

    token = create_new_user_token()
    response.set_cookie(
        key=TOKEN_SYMBOL, value=token, samesite="none", secure=True, httponly=True
    )

    print(token)
    return token


@app.get("/")
async def root():
    return "This is AiMe API"


# Ask
# - Input: message from client
# - Output: message from ai
# Docs: Client sends message to server, server process it calls openai api and returns ai-messages to client
@app.put("/ask/", response_model=ResponseMessage | ResponseDebugMessage)
async def ask(message: AskMessage, token: str = Depends(create_cookie)):
    return service.respond(message.content, token)


# Set Conversation
# - Input: client history
# - Output: success or fail
# Docs: Sends client messages from last conversation to server (it was saved on client inside of local storage)
@app.put("/set-conversation/")
async def set_context(
    history: list[HistoryMessage], token: str = Depends(create_cookie)
):
    service.set_conversation(history, token)


# Reset Conversation
# - Input: nothing
# - Output: success or fail
# Docs: Doing a reset of history on server
@app.put("/reset-conversation/")
async def reset_context(token: str = Depends(create_cookie)):
    service.reset_conversation(token)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
