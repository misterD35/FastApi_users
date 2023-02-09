from fastapi import APIRouter, Request, Depends
from fastapi_jwt import JwtAuthorizationCredentials
from pydantic import typing, SecretStr

from main_dir.config import refresh_security, access_security
from main_dir.models import User, users, refresh_token_for_request

router = APIRouter(tags=['COMMANDS'])


@router.post('/users')
def create_user(data_user: User, request: Request, credentials: JwtAuthorizationCredentials = Depends(refresh_security)):
    token = refresh_token_for_request(request, credentials)
    if token == {'error': 'invalid refresh token'}:
        return token
    if len(users) > 0:
        for user in users:
            if dict(data_user)['id'] == dict(user)['id']:
                return {'status': 'Error! user alrealy exists'}
    users.append(data_user)
    return {'users': users,
            'access_token': access_security.create_access_token(credentials.subject),
            'refresh_token': token}


@router.delete('/users/{user_id}', response_model=typing.List[User])
def delete_users(user_id: int, request: Request, credentials: JwtAuthorizationCredentials = Depends(refresh_security)):
    refresh_token_for_request(request, credentials)
    for user in users:
        if user.id == user_id:
            users.remove(user)
    return users


@router.put('/users/{user_id}', response_model=typing.List[User])
def update_users(user_id: int, user: User, request: Request, credentials: JwtAuthorizationCredentials = Depends(refresh_security)):
    refresh_token_for_request(request, credentials)
    for __user in users:
        if __user.id == user_id:
            __user.username = user.username
            __user.password = user.password
    return users


@router.patch('/users/{user_id}', response_model=typing.List[User])
def update_users_password(user_id: int, password: str, request: Request, credentials: JwtAuthorizationCredentials = Depends(refresh_security)):
    refresh_token_for_request(request, credentials)
    for user in users:
        if user.id == user_id:
            user.password = SecretStr(password)
    return users