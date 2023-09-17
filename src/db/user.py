from src.db.db import db_instance


class UserModel:
    @staticmethod
    def get(token: str) -> str:
        users = list(db_instance.db.keys())

        maybe_user = list(filter(lambda db_token: db_token == token, users))

        if maybe_user:
            return maybe_user[0]

        UserModel.create(token)

        return token

    @staticmethod
    def create(user_token: str) -> str:
        db_instance.db[user_token] = []
        return user_token
