from dotenv import dotenv_values
from langchain.prompts import PromptTemplate

from langchain.schema import AIMessage, HumanMessage, SystemMessage

from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI


from langchain.chains import ConversationChain


# config = dict(dotenv_values(".env"))


# prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
# print(prompt.format(product="colorful socks"))


# model = config["MODEL"]
# api_key = config['OPENAI_API_KEY']
# chat = ChatOpenAI(model_name=model, openai_api_key=api_key)

# messages = [
#     SystemMessage(content="You are a helpful assistant that translates English to French."),
#     HumanMessage(content="I love programming.")
# ]


# result = chat(messages)

# print(result)
