from fastapi import APIRouter, Depends
from fastapi_jwt import JwtAuthorizationCredentials
from main_dir.config import access_security
from main_dir.models import users

router = APIRouter(tags=['USERS'])


@router.get('/users')
def get_users(credentials: JwtAuthorizationCredentials = Depends(access_security)):
    return {'users': users, 'credentials.subject': credentials.subject}


@router.get('/users/who_is')
def get_all_who_users(password: str, credentials: JwtAuthorizationCredentials = Depends(access_security)):
    return {'user': [user for user in users if user.password.get_secret_value() == password], 'credentials.subject': credentials.subject}


@router.get('/is_login_user')
def get_login_from_db(username: str, credentials: JwtAuthorizationCredentials = Depends(access_security)):
    return [user for user in users if user.username == username]
