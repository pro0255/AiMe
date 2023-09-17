from faker import Faker

from src.chat.boilerplate_ai import AI
from src.db.db import DBMessage

faker = Faker(locale="en_US")


class MockAI(AI):
    def respond(self, _: str, _2: list[DBMessage] = []) -> str:
        return faker.paragraph(nb_sentences=3)
