import os


def create_chat_entity():
    env_value = os.getenv("CHAT_ENTITY")

    print(env_value)

    if env_value == "openai":
        from chat.open_ai import OpenAI

        return OpenAI()
    elif env_value == "mock":
        from chat.mock_ai import MockAI

        return MockAI()
    else:
        from chat.debug_ai import DebugAI

        return DebugAI()
