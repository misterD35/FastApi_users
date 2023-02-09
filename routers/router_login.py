from fastapi import APIRouter

from main_dir.config import refresh_security, access_security
from main_dir.fake_db import fake_db

router = APIRouter(tags=['MAIN_LOGIN'])


@router.post('/auth/login')
def login():
    users = {'id': 123, 'username': 'admin', 'role': 'admin'}
    refresh_token = refresh_security.create_refresh_token(users)
    fake_db.append(refresh_token)
    return {'access_token': access_security.create_access_token(users), 'refresh_token': refresh_token}
