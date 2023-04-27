from datetime import datetime, timedelta
from fastapi import APIRouter
from fastapi.security import HTTPBasicCredentials
from app.dependencies import *

router_token = APIRouter(
    prefix='',
    tags=['addition']
)

@router_token.post('/auth/token')
async def login(credentials: HTTPBasicCredentials):
    if credentials.username != 'admin' or credentials.password != 'secret':
        raise HTTPException(status_code=401, detail='Incorrect username or password')

    payload = {'username': credentials.username, "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)}
    access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return {"access_token": access_token, "token_type": "bearer", "expires_in": f"{ACCESS_TOKEN_EXPIRE_MINUTES}"}

