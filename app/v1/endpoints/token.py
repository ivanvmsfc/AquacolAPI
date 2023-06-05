from datetime import datetime, timedelta
from typing import Annotated
from fastapi import APIRouter, Form
from fastapi.security import HTTPBasicCredentials
from app.dependencies import *
import configparser

config = configparser.RawConfigParser()
config.read('config.properties')
token_username = config.get('Credentials', 'token_username')
token_password = config.get('Credentials', 'token_password')


router_token = APIRouter(
    prefix='',
    tags=['addition']
)

@router_token.post('/auth/token')
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    if username != token_username or password != token_password:
        raise HTTPException(status_code=401, detail='Incorrect username or password')

    payload = {'username': username, "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)}
    access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return {"access_token": access_token, "token_type": "bearer", "expires_in": f"{ACCESS_TOKEN_EXPIRE_MINUTES}"}


