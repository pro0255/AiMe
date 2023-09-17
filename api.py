from enum import Enum
import uvicorn
import secrets


from pydantic import BaseModel
from fastapi import FastAPI, Request, Response, Depends

app = FastAPI()
TOKEN_SYMBOL = "TOKEN_SYMBOL"


class AskMessage(BaseModel):
    content: str


class MessageType(str, Enum):
    ai = "ai"
    client = "client"


class HistoryMessage(BaseModel):
    content: str
    type: MessageType


def create_new_user_token():
    return secrets.token_hex(32)


def create_cookie(response: Response, request: Request):
    request_cookie_token = request.cookies.get(TOKEN_SYMBOL)
    if request_cookie_token:
        return request_cookie_token

    token = create_new_user_token()
    response.set_cookie(key=TOKEN_SYMBOL, value=token)
    return token


@app.get("/")
async def root():
    return "This is AiMe API"


# Ask
# - Input: message from client
# - Output: message from ai
# Docs: Client sends message to server, server process it calls openai api and returns ai-messages to client
@app.put("/ask/")
async def ask(message: AskMessage, token: str = Depends(create_cookie)):
    print(f"Asking {message} {token}")
    return f"This is ask message {message}"


# Set Conversation
# - Input: client history
# - Output: success or fail
# Docs: Sends client messages from last conversation to server (it was saved on client inside of local storage)
@app.put("/set-conversation/")
async def set_context(
    history: list[HistoryMessage], token: str = Depends(create_cookie)
):
    return f"Setting a specific context {len(history)}"


# Reset Conversation
# - Input: nothing
# - Output: success or fail
# Docs: Doing a reset of history on server
@app.put("/reset-conversation/")
async def reset_context(token: str = Depends(create_cookie)):
    return f"Reseting a existing context"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
