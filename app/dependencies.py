from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.core.models.database import SessionLocal
import jwt
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Clave secreta para la firma del token
SECRET_KEY = "mysecretkey"

# Tiempo de expiración del token
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("TOKEN_EXP_TIME"))

# Dependencia para verificar el token
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        # Decodifica el token y verifica la firma
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("username")
        if username is None:
            raise HTTPException(status_code=401, detail="Token inválido")

    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")

    except:
        raise HTTPException(status_code=401, detail="Token inválido")
    return username