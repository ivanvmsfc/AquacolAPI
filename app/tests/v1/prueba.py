from fastapi import APIRouter, Request
from app.dependencies import *

router_prueba = APIRouter(
    prefix='',
    tags=['addition']
)

@router_prueba.get("/prueba")
def prueba_execute(request: Request, data: str = None, username: str = Depends(get_current_user), token: str = Depends(oauth2_scheme)):
    # os.system("prueba.py")
    print(username)
    print(token)
    return "Hola"
