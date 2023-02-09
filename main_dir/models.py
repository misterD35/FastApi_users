from pydantic import BaseModel, SecretStr, typing
from main_dir.config import refresh_security
from main_dir.fake_db import fake_db


class User(BaseModel):
    id: int
    username: str
    password: SecretStr


users: typing.List[User] = []


def refresh_token_for_request(request, credentials):
    refresh_token = request.headers.get('Authorization').split(' ')[1]
    if refresh_token not in fake_db:
        return {'error': 'invalid refresh token'}
    fake_db.remove(refresh_token)
    token = refresh_security.create_refresh_token(credentials.subject)
    fake_db.append(token)
    return token
